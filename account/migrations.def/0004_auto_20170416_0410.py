# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170416_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
