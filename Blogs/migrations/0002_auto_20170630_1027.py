# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='is_readlater',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogs',
            name='is_saved',
            field=models.BooleanField(default=False),
        ),
    ]
