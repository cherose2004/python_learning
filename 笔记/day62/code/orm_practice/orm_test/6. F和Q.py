import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_practice.settings")
import django

django.setup()

from app01 import models

# F
ret = models.Book.objects.filter(price__gt=100)
from django.db.models import F

# 比较两个字段的值
# ret=models.Book.objects.filter(sale__gt=F('kucun'))

#  更新所有的字段
# obj = models.Book.objects.get(pk=1)
# obj.sale =100
# obj.save()

# 只更新sale字段
# models.Book.objects.all().update(sale=100)

# 取某个字段的值进行操作
# models.Book.objects.all().update(sale=F('sale')*2+10)


# Q

from django.db.models import Q

ret = models.Book.objects.filter(~Q(Q(pk__gt=3) | Q(pk__lt=2)) & Q(price__gt=50))
print(ret)

