from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    """首页"""
    return render(request, 'index.html')
