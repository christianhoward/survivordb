# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-30 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20160829_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='p_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='season',
            name='s_url',
            field=models.CharField(max_length=255),
        ),
    ]
