URI   

- URL

- URN



REST 

URI表示一个资源

4种请求方式表示4中操作

GET   获取资源

POST  新建资源

PUT  更新资源

DELETE 删除资源



url 

/publishers/

book   

name 

publisher_id



{

​	name:

​	publisher:   /publisher/1/

}



## RESTful API

域名：https://example.org/api/    

路径  名词（复数）表示     不用动词

请求方式   返回结果

GET   获取资源        返回 资源的列表  

GET   /XXXXX/1       返回 一个资源

POST  新建资源      返回 新建的资源

PUT  更新资源        返回 更改后的资源

DELETE 删除资源     返回空内容  也可以是提示 

状态码 

发生错误时 返回错误信息

Hypermedia API   返回的关联的书籍时  尽量返回url 



/books/      GET  POST 

/book/(\d+)/   GET  PUT  DELETE 

序列化器

```python
from rest_framework import serializers
from app01 import models


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    pub_date = serializers.DateTimeField()

    pub = PublisherSerializer(required=False, read_only=True)
    authors = serializers.SerializerMethodField(read_only=True)  # get_字段名

    post_pub = serializers.IntegerField(write_only=True)
    post_author = serializers.ListField(write_only=True)

    def get_authors(self, obj):
        ser_obj = AuthorSerializer(obj.authors.all(), many=True)
        return ser_obj.data

    def create(self, validated_data):
        book_obj = models.Book.objects.create(
            title=validated_data['title'],
            price=validated_data['price'],
            pub_date=validated_data['pub_date'],
            pub_id=validated_data['post_pub']
        )
        book_obj.authors.set(validated_data['post_author'])
        return book_obj

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.price = validated_data.get('price',instance.price)
        instance.pub_date = validated_data.get('pub_date',instance.pub_date)
        instance.pub_id = validated_data.get('post_pub',instance.pub_id)
        instance.save()
        instance.authors.set(validated_data.get('post_authors',instance.authors.all()))
        return instance
```











