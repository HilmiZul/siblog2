# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_auto_20170416_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='type_menu',
            field=models.CharField(choices=[('link', 'Link'), ('page', 'Page'), ('category', 'Category')], max_length=40),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='type_menu',
            field=models.CharField(choices=[('link', 'Link'), ('page', 'Page'), ('category', 'Category')], max_length=40),
        ),
    ]
