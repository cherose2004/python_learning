##   内容回顾

路由

### 1.urlconf

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home,{}, name='home'),

]
```

### 2.正则表达式

r  ^   $  [0-9]  \d  \w   + ?   * {4} 

### 3.分组和命名分组

url上捕获参数  都是字符串

分组

```python
url(r'^blog/([0-9]{4})/(\d{2})$', views.blogs, name='blogs'),
```

捕获的参数会按照位置传参传递给视图函数

命名分组

```python
url(r'^blog/(?P<year>[0-9]{4})/(?P<month>\d{2})$', views.blogs, name='blogs'),
```

捕获的参数会按照关键字传参传递给视图函数

### 4.路由分发 include

```python
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^app01/', include('app01.urls', namespace='app01')),
    url(r'^app02/', include('app02.urls', namespace='app02')),

]
```

### 5.传递参数

```python
  url(r'^home/(?P<year>\d{4})$', views.home,{'year':2019}, name='home'),
```

### 6.url的命名和反向解析

静态路由

命名：

```python
	url(r'^home/$', views.home, name='home'),
```

反向解析：

模板

{% url 'home' %}    ——》   '/app01/home/'

py文件

from django.urls import reverse

reverse('home')    ——》    '/app01/home/'

分组：

命名：

```python
url(r'^blog/([0-9]{4})/(\d{2})$', views.blogs, name='blogs'),
```

反向解析：

模板

{% url 'blogs' '2019' '06' %}    ——》    '/app01/blog/2019/06'

py文件

from django.urls import reverse

reverse('blogs,'args=('2019','07'))    ——》    '/app01/blog/2019/07'

命名分组：

命名：

```python
url(r'^blog/(?P<year>[0-9]{4})/(?P<month>\d{2})$', views.blogs, name='blogs'),
```

反向解析：

模板

{% url 'blogs' '2019' '06' %}    ——》    '/app01/blog/2019/06'     按照位置传参

{% url 'blogs'  month='06' year='2019' %}    ——》    '/app01/blog/2019/06'    按照关键字传参 

py文件

from django.urls import reverse

reverse('blogs,'args=('2019','07'))    ——》    '/app01/blog/2019/07'    按照位置传参

reverse('blogs',kwargs={'year':'2018','month':'08'})     ——》   '/app01/blog/2018/08'     按照关键字传参 

### 7.namespace

```python
 url(r'^app01/', include('app01.urls', namespace='app01')),
```

{% url 'app01:home' %}    ——》   '/app01/home/'

reverse('app01:home')    ——》    '/app01/home/'

## 今日内容

### 1.ORM的字段和参数

```python
AutoField    主键
IntegerField  整数
CharField    字符串
BooleanField  布尔值
TextField    文本
DateTimeField DateField  日期时间
    auto_now_add=True    # 新增数据的时候会自动保存当前的时间
    auto_now=True        # 新增、修改数据的时候会自动保存当前的时间
DecimalField   十进制的小数
	max_digits       小数总长度   5
    decimal_places   小数位长度   2
```

参数：

null                数据库中字段是否可以为空

blank=True    form表单填写时可以为空

default        字段的默认值

db_index    创建索引

unique     唯一

choices=((0, '女'), (1, '男')     可填写的内容和提示

### 2.表的参数

```python
class Meta:
    db_table = "person"  # 表名

    verbose_name = '个人信息'

    verbose_name_plural = '个人信息'

    index_together = [
        ("name", "age"),  # 应为两个存在的字段
    ]
    #
    unique_together = (("name", "age"),)   # 应为两个存在的字段
```

### 3.ORM查询(13条)   必知必会13条

见代码

### 4.单表双下划线

见代码

### 5.外键的操作

见代码