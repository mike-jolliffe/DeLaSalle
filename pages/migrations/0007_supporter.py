# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20171228_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supporter_name', models.CharField(max_length=100)),
                ('player_name', models.CharField(max_length=100)),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supporters', to='pages.Player')),
            ],
        ),
    ]
