# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-25 02:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20190625_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', related_query_name='xxx', to='app01.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='xxx', to='app01.Publisher'),
        ),
    ]