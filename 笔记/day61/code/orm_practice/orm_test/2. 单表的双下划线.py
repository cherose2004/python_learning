import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_practice.settings")
import django

django.setup()

from app01 import models

ret = models.Person.objects.filter(pk__gt=1)   # gt  greater than   大于
ret = models.Person.objects.filter(pk__lt=3)   # lt  less than   小于
ret = models.Person.objects.filter(pk__gte=1)   # gte  greater than   equal    大于等于
ret = models.Person.objects.filter(pk__lte=3)   # lte  less than  equal  小于等于


ret = models.Person.objects.filter(pk__range=[2,3])   # range  范围
ret = models.Person.objects.filter(pk__in=[1,3,10,100])   # in  成员判断

ret = models.Person.objects.filter(name__contains='A')
ret = models.Person.objects.filter(name__icontains='A')   # 忽略大小写

ret = models.Person.objects.filter(name__startswith='a')  # 以什么开头
ret = models.Person.objects.filter(name__istartswith='A')


ret = models.Person.objects.filter(name__endswith='a')  # 以什么结尾
ret = models.Person.objects.filter(name__iendswith='I')


ret  = models.Person.objects.filter(birth__year='2019')
ret  = models.Person.objects.filter(birth__contains='2018-06-24')
ret  = models.Person.objects.filter(phone__isnull=False)

print(ret)