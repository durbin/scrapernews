# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='points',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]