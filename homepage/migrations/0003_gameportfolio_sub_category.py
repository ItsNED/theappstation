# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180528_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameportfolio',
            name='sub_category',
            field=models.CharField(default='전략디펜스', max_length=30),
            preserve_default=False,
        ),
    ]
