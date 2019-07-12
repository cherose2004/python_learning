1.权限

2.为什么要有权限?

让不同的人使用不同的功能

3.开发一个权限的组件,为什么开发组件?

4.web开发中,什么是权限?

url代表权限

5.表结构的设计

第一版

用户表 user

id  username  pwd 

1    alex    123 

2    peiqi   123

权限表  permission

id  url   

1     /customer_list/

2    /customer_add/



用户和权限的关系表

id  user_id  permission_id

1      1              1   

2      1              2

3      2              1

第二版:

用户表 user

id  username  pwd 

1    alex    123 

2    peiqi   123

权限表  permission

id  url   

1     /customer_list/

2    /customer_add/

角色表

id     name

1    BOSS

2     二老板



用户和角色的关系表

id  user_id  role_id

1      1              1   

2      1              2

3      2              1



角色和权限和的关系表

id    role_id  permission_id  

1      1              1   

2      1              2 

6.功能实现

登录

​	查询权限

​	values()    跨表 去重  去空

中间件 

​	白名单  re.match