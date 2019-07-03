from django.db import models


class Publisher(models.Model):
    # id
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)
