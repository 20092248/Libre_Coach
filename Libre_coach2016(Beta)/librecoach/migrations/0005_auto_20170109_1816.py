# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 17:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librecoach', '0004_auto_20161231_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='date_depot',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 9, 18, 16, 54, 568836)),
        ),
        migrations.AlterField(
            model_name='coach',
            name='coach_image',
            field=models.FileField(upload_to=''),
        ),
    ]
