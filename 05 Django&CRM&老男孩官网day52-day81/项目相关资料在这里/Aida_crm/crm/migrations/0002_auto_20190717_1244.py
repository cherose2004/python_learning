# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-17 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='用户所拥有的角色'),
        ),
        migrations.AlterField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(blank=True, to='crm.UserProfile', verbose_name='老师'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='class_list',
            field=models.ManyToManyField(blank=True, to='crm.ClassList', verbose_name='已报班级'),
        ),
    ]
