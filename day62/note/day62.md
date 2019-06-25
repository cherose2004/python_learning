##   内容回顾

### 1.orm

面向对象和关系型数据库的一种映射。通过操作对象的方式操作数据。

对应关系：

类    ——》    表

对象  ——》 数据行

属性   ——》 字段

### 2.常用字段

```
CharField    ——》  varchar(32)
AutoField(primary_key=True)    ——》 主键
DateTimeField
DateField
BooleanField  
IntegerField    
FloatField
DecimalField
TextField
```

### 3.字段的参数

auto_now_add=True   新增时保存当前的时间

auto_now=True     新增或修改时保存当前的时间

default   默认值

verbosename   显示中文

null=True         数据库中该字段可以为null

blank=True      填写form表单时该字段可以为空

choices=((0, '女'), (1, '男'))  

db_column     数据库的列名

unique=True     唯一约束

### 4.model的参数

```
class Person(models.Model):
	    class Meta:
        db_table = "person"  # 表名

        index_together = [
            ("name", "age"),  # 应为两个存在的字段
        ]

        unique_together = (("name", "age"),)  # 应为两个存在的字段
```

### 5.必知必会13条

Person.objects.all()

返回对象列表

all()   		获取所有的数据

filter()       获取所有满足条件的数据

exclude()       获取所有不满足条件的数据

values()    获取对象的字段名和字段值    [ {} ]   

values_list()    获取对象字段值    [ () ]   

order_by()    排序  默认升序  - 降序

reverse()      对已经排序的对象列表进行倒叙排序

distinct()    去重     不支持按字段去重   想去重  数据必须完全一致

返回对象的

get()    获取一个满足条件的对象   获取不到或者多个就报错

first()    取第一个元素   取不到就是None

last()    取最后一个元素   取不到就是None

返回布尔值

exists()     判断查询是否有结果

返回数字

count()    计数

### 6.单表的双下划綫

id=1

__gt  大于

__lt  小于

__gte 

__lte

__range=[1,10]

__in = [1,3,5]

__contains        like 

__icontains     忽略大消息

__startswith   以什么开头

__endswith   以什么结尾

__istartswith 

__iendswith

__year   

__isnull = True  

### 7.外键

表示一对多的关系

```python
class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey(Publisher, related_name='books',related_query_name='xxx',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

基于对象查询

正向

book_obj.pub    ——》  所关联的对象

book_obj.pub_id    ——》  所关联的对象id

反向

没有指定related_name

pub_obj.book_set     ——》  关系管理对象    （类名小写_set）

pub_obj.book_set.all（）   ——》  所关联的所有对象

指定related_name='books'

pub_obj.books   ——》  关系管理对象    （类名小写_set）

pub_obj.books.all（）   ——》  所关联的所有对象



基于字段查询

models.Book.objects.filter(pub__name='xxxxx')



没有指定related_name

models.Publisher.objects.filter(book__title='xxxxx')

指定related_name=‘books’

models.Publisher.objects.filter(books__title='xxxxx')

指定related_query_name='book‘

models.Publisher.objects.filter(book__title='xxxxx')

## 今日内容

### 1.多对多

见代码

### 2.聚合和分组

```python
from app01 import models

from django.db.models import Max, Min, Avg, Sum, Count


ret = models.Book.objects.filter(pk__gt=3).aggregate(Max('price'),avg=Avg('price'))
print(ret)


# 分组
# 统计每一本书的作者个数
ret = models.Book.objects.annotate(count=Count('author')) # annotate 注释


# 统计出每个出版社的最便宜的书的价格
# 方式一
ret = models.Publisher.objects.annotate(Min('book__price')).values()
# 方式二
ret = models.Book.objects.values('pub_id').annotate(min=Min('price'))

```

### 3.F和Q

```python
from django.db.models import F

# 比较两个字段的值
ret=models.Book.objects.filter(sale__gt=F('kucun'))

# 只更新sale字段
models.Book.objects.all().update(sale=100)

# 取某个字段的值进行操作
models.Book.objects.all().update(sale=F('sale')*2+10)
```

Q(条件)

|  或

&  与 

~ 非

```
from django.db.models import Q

ret = models.Book.objects.filter(Q(Q(pk__gt=3) | Q(pk__lt=2)) & Q(price__gt=50))
print(ret)
```

### 4.事务

```python
from django.db import transaction

try:
    with transaction.atomic():
        # 进行一系列的ORM操作

        models.Publisher.objects.create(name='xxxxx')
        models.Publisher.objects.create(name='xxx22')

except Exception as e :
    print(e)
```