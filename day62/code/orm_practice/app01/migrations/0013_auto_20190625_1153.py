# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-25 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='kucun',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='sale',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='app01.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher'),
        ),
    ]
