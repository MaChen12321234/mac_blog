from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import title
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from scrapy.http import JsonRequest
from unicodedata import category
from .models import BlogCategory, BlogContext, BlogComment
from .forms import PubBlogForm
from django.http.response import JsonResponse

from zl_auth.views import zlogin


# Create your views here.


def index(request):
    """首页"""
    return render(request, 'index.html')


@require_http_methods(['GET', 'POST'])
@login_required()
def blog_pub(request):
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request, 'pub-blog.html', context={"categories": categories})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            blog = BlogContext.objects.create(title=title, content=content, category_id=category_id, author=request.user)
            return JsonResponse({"code": 200, "message": "博客发布成功！", "data": {"blog_id": blog.id}})
        else:
            print(form.errors)
            return JsonResponse({'code': 400, "message": "参数错误！"})

def blog_detail(request, bid):
    return render(request, 'blog_detail.html', {'bid': bid})
