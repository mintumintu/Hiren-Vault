# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 02:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0003_tag_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 4, 22, 2, 17, 57, 645690, tzinfo=utc)),
            preserve_default=False,
        ),
    ]