# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-30 00:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20160815_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['lastname', 'firstname']},
        ),
    ]
