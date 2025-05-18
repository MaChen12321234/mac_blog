from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='分类')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogContext(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='分类')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    class Meta:
        verbose_name = '博客内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',  verbose_name='作者')
    content = models.TextField(verbose_name='内容')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    blog = models.ForeignKey(BlogContext, on_delete=models.CASCADE, verbose_name='博客')

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
