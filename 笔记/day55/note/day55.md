# 内容回顾

### 1.django的命令

下载安装

pip install django==1.11.21 -i 源

创建项目

django-admin startproject 项目名称

启动

cd 项目的根目录下  manage.py

python manage.py runserver   #  127.0.0.1:8000

python manage.py runserver 80   #  127.0.0.1:80

python manage.py runserver 0.0.0.0:80   #  0.0.0.0:80

创建APP

python manag.py  startapp app名称

数据库迁移的命令

python manage.py makemigrations   # 记录models.py的变更记录

python manage.py migrate   # 迁移  将变更记录同步到数据库中

### 2.django的配置

静态文件

STATIC_URL = '/static/'    

STATICFILES_DIRS=[

​	os.path.join(BASE_DIR,‘static’)，

​	os.path.join(BASE_DIR,‘static1’)，

]



数据库  DATABASES

ENGINE  引擎 

NAME     数据库的名称

HOST   IP    '127.0.0.1'  

PORT   端口号   3306 

USER  用户名

PASSWORD 密码



INSTALLED_APPS

'app01'

'app01.apps.App01Config'



中间件  

注释  'django.middleware.csrf.CsrfViewMiddleware'    可以提交POST请求



TEMPLATES 

'DIRS': [os.path.join(BASE_DIR, 'templates')]

### 3.django使用MySQL数据库的流程

1.创建一个MySQL数据库；

2.在settings中配置数据库；

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'day53',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123'

    }
}
```

3.让django使用pymysql连接MySQL数据库

在与settings同级目录下的init 中写：

```python
import pymysql
pymysql.install_as_MySQLdb()
```

4.创建表  在app下的models.py中写类（集成models.Model）

```python
from django.db import models

class User(models.Model):   # app名称_user
    pid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)   # username varchar(32)
    password = models.CharField(max_length=32)   # password varchar(32)
```

5.执行数据库迁移的命令

python manage.py makemigrations   # 记录models.py的变更记录

python manage.py migrate   # 迁移  将变更记录同步到数据库中

### 4.get和post

get  获取到一个资源

发get的途径：

1.在浏览器的地址栏种输入URL，回车

2.a标签

3.form表单   不指定 method    method=‘get’

传递参数     url路径?id=1&name=alex

django种获取url上的参数    request.GET   {'id':1,'name':'alex'}   request.GET.get(key)     request.GET[key]



post   提交数据.

form表单   method=‘post’   

参数不暴露在URL    在请求体中  

django中获取post的数据  request.POST 

### 5.ORM 

对应关系

类     —— 》    数据表

对象   ——》  数据行（记录）

属性  ——》   字段

from app01 import models 

查：

models.Publisher.objects.all()   ——》  查询所有的数据    queryset  对象列表  

models.Publisher.objects.get(name='xxxx')     ——》 对象      获取不到或者获取到多个就报错

models.Publisher.objects.filter(name='xxxx')   ——》 获取满足条件的所有的对象   queryset  对象列表   

增：

models.Publisher.objects.create(name='xxx')   ——》  新插入数据库的对象

obj = models.Publisher(name='xxx')  ——》 存在在内存中的对象

obj.save()      ——》   提交到数据库中  新增

删：

obj = models.Publisher.objects.get(pk=1)

obj.delete()  

obj_list = models.Publisher.objects.filter(pk=1)

obj_list.delete()

改：

obj = models.Publisher.objects.get(pk=1)

obj.name  = 'new name'      ——》 在内存中修改对象的属性

obj.save()      ——》   提交数据   保存到数据库中



# 今日内容

图书管理

书籍管理 

book  

name 

```python 
class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)
```

on_delete  在django2.0 版本之后是必填的参数    1.11  之前的可以不填 

on_delete 的参数  models.CASCADE  models.SET()  models.SET_DEFAULT   models.SET_NULL

查询

```python
all_books = models.Book.objects.all()

for book in all_books:

    print(book.title)
    print(book.pub,type(book.pub))   #  ——> 所关联的出版社对象
    print(book.pub.pk)  #  查id 多一次查询
    print(book.pub_id)  # 直接在book表中查出的ID
    print(book.pub.name)
    print("*"*32)
```

新增

```python
models.Book.objects.create(title=book_name,pub=出版社的对象)
models.Book.objects.create(title=book_name,pub_id=pub_id)
```

删除

```python
pk = request.GET.get('id')
models.Book.objects.filter(pk=pk).delete()
```

编辑

```HTML
{% if book_obj.pub == publisher %}
    <option selected value="{{ publisher.pk }}"> {{ publisher.name }} </option>
{% else %}
    <option  value="{{ publisher.pk }}"> {{ publisher.name }} </option>
{% endif %}
```

```python
# 修改数据
book_obj.title = book_name
# book_obj.pub_id = pub_id
book_obj.pub = models.Publisher.objects.get(pk=pub_id)
book_obj.save()
```



