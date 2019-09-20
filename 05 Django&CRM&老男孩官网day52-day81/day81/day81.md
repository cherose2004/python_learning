restful API

1. 协议  推荐使用https

2. 域名

   api.域名    

   域名/api/

3. 版本

   路径/v1/

   版本加到请求头中

4. url  不用有动词  使用名词

   /books/ 

   /book/\d+

5. 请求方法

   get   获取资源  所有/单个

   post   新增自增

   put   更新资源

   delete  删除资源

6. 状态码

   200     201  204 

   401    403   404  

7. 返回不同结果

   /books/ 

   get  返回所有的数据

   poet   返回新增的数据      

   /book/\d+/

   get  返回单个的数据

   put  返回更新后的数据

   delete   返回空   返回提示

8. 出错误  返回错误信息

9. 过滤条件 

   ?page=1&page_size=100 

   ?type=1 

10. 返回相关数据时  返回链接

django  

djangorestframework

rest_framework

推荐使用CBV

```
from rest_framework.views import APIView
from rest_framework.response import Response
```

序列化     json 

对象 等数据类型类型  ——》  可用用于传输/存储的数据形式      

序列化器

```python
from rest_framework import serializers

class  BookSerializer(serializers.Serializer):
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

```



### 极验验证码

所需模块

geetest

requests

文档地址：<https://docs.geetest.com/install/overview/start/>

### aliyun短信

所需模块

aliyun-python-sdk-core

文档地址：

<https://help.aliyun.com/document_detail/53090.html?spm=a2c1g.8271268.10000.94.772fdf25kEccNH>

[https://api.aliyun.com/new#/?product=Dysmsapi&api=SendSms&params=%7B%22RegionId%22%3A%22cn-hangzhou%22%2C%22PhoneNumbers%22%3A%22%22%2C%22SignName%22%3A%22%22%2C%22TemplateCode%22%3A%22%22%7D&tab=DEMO&lang=JAVA](https://api.aliyun.com/new#/?product=Dysmsapi&api=SendSms&params={"RegionId"%3A"cn-hangzhou"%2C"PhoneNumbers"%3A""%2C"SignName"%3A""%2C"TemplateCode"%3A""}&tab=DEMO&lang=JAVA)











