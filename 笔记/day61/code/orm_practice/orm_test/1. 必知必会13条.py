import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_practice.settings")
import django

django.setup()

from app01 import models

#  all()   获取所有的数据   ——》 QuerySet   对象列表

ret = models.Person.objects.all()

# get()    获取满足条件的一个数据   ——》 对象
#  获取不到或者多个都报错

ret = models.Person.objects.get(pk=1)


# filter()    获取满足条件的所有数据   ——》 QuerySet   对象列表


ret = models.Person.objects.filter(pk=1)

# exclude()    获取不满足条件的所有数据   ——》 QuerySet   对象列表

ret = models.Person.objects.exclude(pk=1)


# values()        拿到对象所有的字段和字段的值    QuerySet  [ {} ,{} ]
# values('字段')   拿到对象指定的字段和字段的值    QuerySet  [ {} ,{} ]

ret = models.Person.objects.values('pid','name')

# values_list()     拿到对象所有的字段的值    QuerySet  [ () ,() ]
# values('字段')   拿到对象指定的字段的值      QuerySet  [ {} ,{} ]
ret = models.Person.objects.values_list('name','pid')

# order_by  排序   - 降序    ——》 QuerySet  [ () ,() ]
ret = models.Person.objects.all().order_by('age','-pid')

# reverse  反向排序   只能对已经排序的QuerySet进行反转
ret = models.Person.objects.all()
ret = models.Person.objects.all().reverse()

# distinct 去重  完全相同的内容才能去重
ret = models.Person.objects.values('age').distinct()


#  count()  计数
ret = models.Person.objects.all().count()

# first  取第一元素   没有元素 None
ret = models.Person.objects.filter(pk=1).values().first()

# last  取最后一元素   没有元素 None


# exists 查询的数据是否存在
ret = models.Person.objects.filter(pk=1000).exists()

print(ret)


"""
返回queryset
all()    
filter()
exclude()
values()  
values_list() 
order_by() 
reverse() 
distinct()

返回对象
get() 
first()
last()

返回数字
count()

返回布尔值的
exists()
"""


