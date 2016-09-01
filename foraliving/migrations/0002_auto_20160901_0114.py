# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-01 05:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foraliving', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
