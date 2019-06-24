# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20190624_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.BooleanField(choices=[(0, '女'), (1, '男')], verbose_name='性别'),
        ),
        migrations.AlterModelTable(
            name='person',
            table='person',
        ),
    ]
