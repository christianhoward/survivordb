# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-30 01:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20160829_2006'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='pxs',
            order_with_respect_to='pid',
        ),
    ]
