# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20171212_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='teammate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
