from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    print("hello world")
    return render(request, 'index.html')
