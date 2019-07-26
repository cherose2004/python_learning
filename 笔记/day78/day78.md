文章

类别表

- 列表的名称

  

文章表

- title 
- categary  外键关联
- create_at  datetime
-  summary 摘要

文章详情表

- content textfield



文章表

id    detail_id  

3       1 

文章表详情表

id   contnet 

1      'askjhwqhwqlkhwqlcalkjawehrewlkjaasa'





用户表

博客表

分类

文章表

文章详情





media的配置

settings的配置

```
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

url的配置

```python
from django.views.static import serve
from django.conf import settings

urlpatterns = [
 
    url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
```

富文本编辑框

下载 

pip install django-ckeditor

注册

```
INSTALLED_APPS = [
	
    'ckeditor',
    'ckeditor_uploader',
]
```

使用字段：

```
from ckeditor_uploader.fields import RichTextUploadingField


class ArticleDetail(models.Model):
    content = RichTextUploadingField(verbose_name='文章详情')
```

配置URL：

```python
from ckeditor_uploader import views

urlpatterns = [

    url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    # 上传文件
    url(r'^ckeditor/upload/', views.upload),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
```

模板中：

```

{{ field }}   富文本编辑框的字段

<script src="{% static 'ckeditor/ckeditor/ckeditor.js' %}"></script>
<script src="{% static 'ckeditor/ckeditor-init.js' %}"></script>
```

