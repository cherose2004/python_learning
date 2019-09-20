## 内容回顾

1.公户和私户的转换

公户  客户没有销售 

私户  客户绑定一个销售

2.模糊查询

filter（Q(__contains=query)|Q()）

```
Q(Q(qq__contains=query) | Q(name__contains=query) | Q(phone__contains=query))

field_list = []
q = Q()
q.connector = 'OR'
#q.children.append(Q(qq__contains=query))

# Q(qq__contains=query)  ——》   Q(('qq__contains',query))
for field in field_list:
	q.children.append( Q(('{}__contains'.format(field),query)) )
```

3.分页保留搜索条件

QueryDict    {} 

qd = QueryDict(mutable=Ture)

qd['page'] = 1 

qd['query'] = 123

qd.urlencode()    =>   page=1&query=123

request.GET.copy()    深拷贝  可编辑

4.编辑后跳转到源页面

simple_tag

QueryDict  



1.跟进记录的管理

展示当前销售的所有的跟进记录

展示某一个客户的所有的跟进记录

新增和编辑跟进记录

- 限制条件
  - 限制跟进客户是当前销售的私户
  - 限制销售是当前用户

2.报名表的管理

