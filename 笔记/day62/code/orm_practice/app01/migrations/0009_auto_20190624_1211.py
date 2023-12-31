# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20190624_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
            ],
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': '个人信息', 'verbose_name_plural': '个人信息'},
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('name', 'age')]),
        ),
        migrations.AlterIndexTogether(
            name='person',
            index_together=set([('name', 'age')]),
        ),
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher'),
        ),
    ]
