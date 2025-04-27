from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    print("push test")
    return render(request, 'index.html')
