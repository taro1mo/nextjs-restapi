from re import T
from django.contrib import admin
from .models import Task, Post

admin.site.register(Post)
admin.site.register(Task)