# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-29 18:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('librecoach', '0019_auto_20161229_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librecoach.Coach'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='date_depot',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 29, 19, 5, 50, 313650)),
        ),
        migrations.AlterField(
            model_name='coach',
            name='coach_image',
            field=models.CharField(default='---------', max_length=1000),
        ),
    ]
