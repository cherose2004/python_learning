## 内容回顾

RBAC   基于角色权限控制

表结构的设计

权限表

- url   权限  正则表达式  ^ $ 
- title  标题 

角色表

- name  角色的名称

- permissions  多对多

角色和权限的关系表

- role_id 
- permission_id

用户表

- username  
- password  
- roles 多对多 

用户和角色关系表

- user_id

- role_id 

一级菜单

权限表

- url
- title
- is_menu 
- icon 

二级菜单

菜单表

- title   
- icon  

权限表

- url
- title
- menu  外键  关联菜单表



权限的列表

permission_list  = [  { 'url':  url  } ,{ 'url':  url  }  ]

菜单的字典

menu_dict = {

​	 一级菜单的id: {

​					title  

​					icon

​					children :  [   

​								{   'url'   'title '   }

​					   ]  

​			}

}



一级菜单的排序

```python
from collections import OrderedDict
sorted(menu_dict, key=lambda x: menu_dict[x]['weight'], reverse=True)
```



财务管理

​	  缴费列表

​			添加缴费

​			编辑缴费

客户管理

​	客户列表

​		添加缴费

​		编辑缴费



permission

id      url                            title             menu_id     parent_id 

1    /payment/list/         缴费列表      1                      null  

2   /payment/add/    	添加缴费     null                  1 

3   /payment/edit/        编辑缴费     null                  1



