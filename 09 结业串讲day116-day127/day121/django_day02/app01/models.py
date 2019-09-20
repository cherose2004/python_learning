from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    classes = models.ForeignKey('Classes', on_delete=models.CASCADE)


class Classes(models.Model):
    name = models.CharField(max_length=32, verbose_name="班级")
