# -*- coding: utf-8 -*-
# __author__ = "maple"


import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_practice.settings")
import django

django.setup()

from app01 import models

from django.db.models import Max, Min, Avg, Sum, Count

# ret = models.Book.objects.filter(pk__gt=3).aggregate(Max('price'),avg=Avg('price'))
# print(ret)


# 统计每一本书的作者个数
ret = models.Book.objects.annotate(count=Count('author')) # annotate 注释


# 统计出每个出版社的最便宜的书的价格
# 方式一
ret = models.Publisher.objects.annotate(Min('book__price')).values()
# 方式二
ret = models.Book.objects.values('pub_id').annotate(min=Min('price'))

# 统计不止一个作者的图书
ret = models.Book.objects.annotate(count=Count('author')).filter(count__gt=1)

# 查询各个作者出的书的总价格
ret = models.Author.objects.annotate(Sum('books__price')).values()
print(ret)

