from django.contrib import admin
from .models import Post
from django_markdown.admin import MarkdownModelAdmin
from django.contrib import admin

admin.autodiscover()

admin.site.register(Post, MarkdownModelAdmin)