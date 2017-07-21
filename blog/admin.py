from django.contrib import admin
from .models import Post
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(Post, MarkdownModelAdmin)