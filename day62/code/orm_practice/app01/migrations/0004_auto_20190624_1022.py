# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 02:22
from __future__ import unicode_literals

import app01.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20190624_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(db_column='username', max_length=32),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=app01.models.MyCharField(blank=True, max_length=11, null=True),
        ),
    ]