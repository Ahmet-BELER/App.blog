from django.contrib import admin
from .models import Profile, Category, Post, Comment, PostView, Like
# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
