# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class App01Author(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'app01_author'


class App01Authorbook(models.Model):
    date = models.DateField()
    author = models.ForeignKey(App01Author, models.DO_NOTHING)
    book = models.ForeignKey('App01Book', models.DO_NOTHING)
    tuijian = models.ForeignKey(App01Author, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app01_authorbook'


class App01Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('App01Publisher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app01_book'


class Publisher(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    addr = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app01_publisher'
