djangorestframework使用

1. 下载安装

```python
pip install djangorestframework  ## djangorestframework
pip install django-filter  ## 过滤使用

```

2. 注册

```python
INSTALLED_APPS = [
	...
    'rest_framework',
    'django_filters'
]
```

3. model

```python
class Feedback(models.Model):
    type_choice = (
        (0, '未分类'),
        (1, '学习笔记'),
        (2, '学员评价'),
        (3, '入职邀约'),
    )

    img = models.ImageField(upload_to='img/feedback/')
    back_type = models.IntegerField(choices=type_choice, default=0)
```

4. 路由

```
url(r'^ajax_feedback/', views.AjaxFeedback.as_view()),
```

5. 视图

```python
from rest_framework import generics
from web.serializers import FeedbackSerializer
from web.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend


class AjaxFeedback(generics.ListAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = FeedbackSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['back_type']
```

6. 序列化器类

```python
from rest_framework import serializers
from repository import models


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = ['img']

```

7. 分页类

```python

from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination):
    page_size = 8  # 一页多少条数据
    page_query_param = 'page'  # 分页查询条件的key
    page_size_query_param = 'size'
    # max_page_size = 8

```

