1.信息展示

ORM操作

all_customers = models.Customer.objects.all()

1.普通字段

对象.字段   ——》数据库中的值

2.有choices参数

对象.字段   ——》数据库中的值

`对象.get_字段_display()`     ——》数据库中的值对应的中文

3.外键

对象.外键字段   ——》所关联的对象    `__str__`

对象.外键.name  

4.自定义方法

1. 多对多

   ```python
   def show_class(self):
       return '|'.join([  str(i) for i in self.class_list.all() ])
   ```

2. 自定义的需求

   返回HTML标签

   ```python
   from django.utils.safestring import mark_safe
       
       
       def show_status(self):
           color_dict = {
               'signed': "green",
               'unregistered': 'red',
               'studying': 'blue',
               'paid_in_full': 'gold'
           }
   
           return mark_safe(
               '<span style="color: white;background: {};padding: 5px" >{}</span>'.format(color_dict.get(self.status),self.get_status_display()))
   
   
   ```

2.分页

需求：

- 新增客户（modelform）
  - get    返回一个页面 （form表单） 
  - post  提交数据  校验后保存到数据库
- 公户的展示
  - 筛选出没有销售的客户
- 私户的展示
  - 筛选出当前登录用户的客户