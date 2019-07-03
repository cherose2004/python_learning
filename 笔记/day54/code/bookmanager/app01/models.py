from django.db import models


class Publisher(models.Model):
    # id
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,unique=True)
