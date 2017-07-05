# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(verbose_name='Image', default=None, upload_to=blog.models.get_image_filename),
        ),
    ]
