# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockplot', '0004_auto_20160418_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='depot',
            name='value',
            field=models.IntegerField(default=100000),
            preserve_default=False,
        ),
    ]
