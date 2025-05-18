from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/pub/', views.blog_pub, name='blog_pub'),
    path('blog/detail/<int:bid>/', views.blog_detail, name='blog_detail'),
    path('blog/comment/pub/', views.pub_comment, name='pub_comment'),
]