# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-23 18:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librecoach', '0010_auto_20161223_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='date_depot',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 23, 19, 22, 24, 540140)),
        ),
    ]
