# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_mymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=django_markdown.models.MarkdownField(default=False),
        ),
    ]
