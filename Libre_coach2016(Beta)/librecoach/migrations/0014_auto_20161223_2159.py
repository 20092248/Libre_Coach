# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-23 20:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librecoach', '0013_auto_20161223_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='username',
            field=models.CharField(default='-------', max_length=30),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='date_depot',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 23, 21, 59, 50, 248434)),
        ),
    ]
