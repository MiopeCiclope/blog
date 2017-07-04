# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default=datetime.datetime(2017, 7, 4, 13, 51, 14, 725187, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
