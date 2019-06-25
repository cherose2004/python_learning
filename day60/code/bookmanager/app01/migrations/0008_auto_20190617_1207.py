# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-17 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_author_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorbook',
            name='tuijian',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='b', to='app01.Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authorbook',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a', to='app01.Author'),
        ),
    ]