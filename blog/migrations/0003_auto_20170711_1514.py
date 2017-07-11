# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='drunk',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='garbage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='love',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=200, default='You should add a caption'),
        ),
    ]
