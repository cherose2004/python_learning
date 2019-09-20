## 内容回顾

1.展示客户信息

1.普通字段

对象.字段   ——》 数据库中的值

2.choice参数

对象.字段   ——》 数据库中的值

`对象.get_字段_display（）`       ——》 中文的提示

3.外键

对象.外键   ——》 所关联的对象    `__str__`

对象.外键.name   

4.自定义方法

多对多：

```python
	class Customer（）：
	def show_class(self):
        return '|'.join([ str(i)  for i in self.class_list.all()])
        
```

HTML：

2.新增和编辑客户信息

modelform

3.公户和私户的展示

filter()

今日内容：

1.公户和私户的转换

2.模糊查询

```
q = Q()
q.connector = 'OR'
q.children.append(Q(qq__contains=query))

Q(('qq__contains',query))   Q(qq__contains=query) 
```

3.分页保留搜索条件

```python
request.GET   <class 'django.http.request.QueryDict'>   'query': ['13']  
request.GET.urlencode()    ——》  query=13&page=1
request.GET._mutable = True  # 可编辑
request.GET.copy()   # 深拷贝 可编辑
QueryDict(mutable=True)   # 可编辑
```

4.编辑后跳转到源页面

```python
/crm/edit_customer/5/?next=/crm/customer_list/?query=13&page=2
```





