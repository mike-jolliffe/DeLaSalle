# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20171214_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
