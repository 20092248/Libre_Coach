# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-29 18:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librecoach', '0018_auto_20161229_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='date_depot',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 29, 19, 3, 19, 989330)),
        ),
        migrations.AlterField(
            model_name='coach',
            name='coach_image',
            field=models.CharField(max_length=1000),
        ),
    ]
