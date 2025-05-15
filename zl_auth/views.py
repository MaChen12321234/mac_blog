import random
import string

from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from pkg_resources import require
from twisted.plugins.twisted_reactors import default
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.models import User

from .models import CaptchaModel

User = get_user_model()

# Create your views here.

@require_http_methods(['GET', 'POST'])
def zlogin(request):
    """登录"""
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                # 判断是否需要记住密码
                if not remember:
                    # 如果没有选择记住密码，过期时间设置为0
                    request.session.set_expiry(0)
                # 如果选择了记住密码则默认两周过期
                return redirect('/')
            else:
                print('邮箱或者密码错误')
                # form.add_error('password', '邮箱或者密码错误')
                # return render(request, 'login.html', {'form': form})
                return redirect(reverse('zl_auth:zlogin'))

@require_http_methods(['GET', 'POST'])
def register(request):
    """注册"""
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            User.objects.create_user(username=username, password=password, email=email)
            return redirect(reverse('zl_auth:login'))
        else:
            print(form.errors)
            return redirect(reverse('zl_auth:register'))


def zlogout(request):
    logout(request)
    return redirect(reverse('zl_auth:login'))

def send_email_captcha(request):
    """发送邮箱验证码"""
    # 获取邮箱
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'message': '必须传递有限！'})

    # 获取随机四位验证码
    captcha = "".join(random.sample(string.digits, 4))

    # 存储到数据库
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})

    # 发送邮箱
    send_mail('知了博客注册验证', message=f'您的注册验证码是{captcha}', recipient_list=[email], from_email=None)



    return JsonResponse({'code': 200, 'message':'邮箱发送成功'})

