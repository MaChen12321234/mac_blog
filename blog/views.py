from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    print("gitee push test")
    return render(request, 'index.html')
