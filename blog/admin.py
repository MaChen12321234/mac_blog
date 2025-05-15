from django.contrib import admin
from .models import BlogCategory, BlogContext, BlogComment

# Register your models here.

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class BlogContextAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'category', 'pub_time', 'author']


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'author', 'content', 'pub_time']


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogContext, BlogContextAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)