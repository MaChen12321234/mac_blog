from django.urls import path
from . import views

app_name = 'zl_auth'

urlpatterns = [
    path('zlogin/', views.zlogin, name='login'),
    path('register/', views.register, name='register'),
    path('captcha/', views.send_email_captcha, name='send_email_captcha'),
]