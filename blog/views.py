from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    """首页"""
    return render(request, 'index.html')


def blog_pub(request):
    """博客发布编辑"""
    return render(request, 'pub-blog.html')


def blog_detail(request, bid):
    return render(request, 'blog_detail.html', {'bid': bid})
