# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
