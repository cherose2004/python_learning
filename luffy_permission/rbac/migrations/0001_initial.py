# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-11 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='url地址')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='角色名称')),
                ('permissions', models.ManyToManyField(to='rbac.Permission', verbose_name='角色所拥有的权限')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('roles', models.ManyToManyField(to='rbac.Role', verbose_name='用户所拥有的角色')),
            ],
        ),
    ]
