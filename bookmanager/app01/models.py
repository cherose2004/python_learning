from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32, )


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateTimeField(default='2019-01-01 10:10:10')
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')
