# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0002_auto_20170526_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='hacker',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]