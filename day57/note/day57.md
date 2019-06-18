## 内容回顾

### 1.django中所有的命令

下载安装

pip  install django==1.11.21  -i 源

创建项目

django-admin startproject   项目名称

启动项目

cd 项目根目录下

python manage.py  runserver   # 127.0.0.1:8000

python manage.py  runserver   80 # 127.0.0.1:80

python manage.py  runserver   0.0.0.0:80 # 0.0.0.0:80

创建app

python manage.py  startapp  app名称

数据库迁移

pyhton manage.py makemigrations

pyhton manage.py migrate

### 2.配置

静态文件

STATIC_URL = '/static/' 

STATICFILES_DIRS = [

​	os.path.join(BASE_DIR,‘static’)，

]

模板  TEMPLATES  DIRS  [os.path.join(BASE_DIR,‘templates’)，]

数据库  DATABASES

ENGINE 引擎

NAME   数据库的名称

HOST   ip

PORT   端口   3306

USER  用户民

PASSWORD 密码

app   INSTALLED_APPS  =[  'app01'   'app01.apps.App01Config' ]

中间件  MIDDLEWARE     注释csrf相关的中间   提交POST请求

### 3.request

request.method    ——》  请求方式 GET POST 

request.GET           ——》   url上携带的参数     ?name=ddd&id=11    {}

request.POST        ——》   form表单提交的POST请求的数据   {}

### 4.响应

HttpResponse('字符串')       ——》  字符串

render(request,'模板的文件名',{k1:v1})       ——》 返回的是一个完整的页面

redirect('/index/')    ——》  重定向     Location ： /index/

### 5.ORM

```python
from django.db import models

class Publisher(models.Model):   # app01_publisher
    pid = models.AutoField(primary_key=Ture)
    name = models.CharField(max_length=32)   # varchar(32)
    
class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher',on_delete=models.CASCADE)  # pub_id
    
class Author(models.Model):
    name = models.CharField(max_length=32)   # varchar(32)
    books = models.ManyToManyField('Book')
```

```python
from app01 import models
# 查询
models.Publisher.objects.all()  # 查询所有的数据  queryset   对象列表
models.Publisher.objects.get(name='xxx',pid=1)   # Publisher对象  查询不到或者多个 就报错
models.Publisher.objects.filter(name='xxx',pid=1)   # 查询满足条件的所有对象    对象列表
models.Publisher.objects.all().order_by('id')  # 排序  默认升序


pub_obj.pid  pub_obj.pk 
pub_obj.name

book_obj.pub   ——》 所关联的对象
book_obj.pub_id   ——》所关联的对象id


author_obj.books    ——》 关系管理对象
author_obj.books.all()    ——》 所关联的所有对象

# 新增
models.Publisher.objects.create(name='xxxx')

models.Book.objects.create(title='xxxx',pub=Publisher的对象)
models.Book.objects.create(title='xxxx',pub_id=Publisher的对象id)

author_obj = models.Author.objects.create(name='xxxx')
author_obj.books.set([书籍对象的id,书籍对象的id,书籍对象的id])   #  每次都是重新设置

# 删除

models.Publisher.objects.get(pk=1).delete()
models.Publisher.objects.filter(pk=1).delete()

# 修改
pub_obj.name = 'xxxx'
pub_obj.save()

book_obj.title = 'xxx'
book_obj.pub = publisher的对象
book_obj.pub_id = publisher的对象的id
book_obj.save() 


author_obj.name = 'xxx'
author_obj.save()
author_obj.books.set([id,id])
```

## 今日内容

### MVC 和 MTV

MVC 

M: model  模型

V：view   视图   - HTML 

C: controller  控制器   ——路由 传递指令  业务逻辑

MTV：

M： model  模型 ORM

T:    tempalte  模板  - HTML

V：view   业务逻辑

### 模板 - 变量

变量  {{  }}  

.索引  .key  .属性  .方法

### Filter 过滤器

语法： {{ value|filter_name:参数 }}

#### default

```
{{ value|default:"nothing"}}  # 变量不存在或者为空  显示默认值
```

#### filesizeformat

 文件大小

#### add    

相当于+    加法    字符串的拼接   列表的拼接

#### slice

```
{{ hobby|slice:'-2:0:-1' }}
```

#### date

```
{{ now|date:'Y-m-d H:i:s' }}
```

setting中的配置：

```python
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
```

#### safe 

告诉django不需要转义

### 自定义filter

1.在app下创建一个名为tempplatetags的python包；

2.在python中创建py文件,文件名自定义（my_tags.py）;

3.在py文件中写：

```python
from django import template

register = template.Library()  # register也不能变
```

4.写函数+装饰器

```python
@register.filter
def add_xx(value, arg):  # 最多有两个

    return '{}-{}'.format(value, arg)
```

使用：

```html
{% load my_tags %}
{{ 'alex'|add_xx:'dsb' }}
```















