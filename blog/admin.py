from django.contrib import admin
from .models import Post, MyModel
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(MyModel, MarkdownModelAdmin)
admin.site.register(Post)