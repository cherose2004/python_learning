## 内容回顾

rbac 

## 1.表结构

菜单表

- title  标题
- icon  图标
- weight 权限

权限表

- url   权限 url路径 正则表达式  ^$   

- title  标题

- name  url的别名  唯一

- menu  外键    关联菜单表   blank  null     有menu_id  当前的权限是二级菜单 没有menu_id  当前的权限是普通权限

- parent  子关联  没有parent_id   父权限   有parent_id   子权限  

    is_menu  布尔   一级菜单使用的

    icon 		一级菜单使用的

角色表

- name   角色的名称
- permissions  多对多 关联权限表

用户表

- username 
- password
- roles    多对多 关联角色表

角色和权限的关系表

用户和角色的关系表

## 2.流程

### 简单的权限控制

1. 登录成功保存权限信息到session中

   权限的数据结构：

   ​		permission_list = [  {  url  }]

2. 中间件

   - 获取当前访问的url路径
   - 白名单
   - 登录状态的校验
   - 免认证的校验
   - 权限的校验
     - 从session中获取权限
     - 循环权限   正则匹配  

3. 模板

   - 母版和继承 

   

### 动态生成一级菜单

1. 登录成功保存权限信息和菜单信息到session中

   权限的数据结构：

   ​		permission_list = [  {  url  }]

   菜单的数据结构：

   ​		menu_list =  [  { url   title   } ]

2. 中间件

   - 获取当前访问的url路径
   - 白名单
   - 登录状态的校验
   - 免认证的校验
   - 权限的校验
     - 从session中获取权限
     - 循环权限   正则匹配  

3. 模板

   - 母版和继承 
   - 动态生成一级菜单
     - inclusion_tag 
     - 一层for循环 menu_list 

   

### 动态生成二级菜单

1. 登录成功保存权限信息和菜单信息到session中

   权限的数据结构：

   ​		permission_list = [  {  url  }]

   菜单的数据结构：

   ​		menu_dict = {  

   ​				一级菜单的ID： {  

   ​							title   icon   children： [  {  url   title }  ]

   ​				 }

   ​		}

2. 中间件

   - 获取当前访问的url路径
   - 白名单
   - 登录状态的校验
   - 免认证的校验
   - 权限的校验
     - 从session中获取权限
     - 循环权限   正则匹配  

3. 模板

   - 母版和继承 
   - 动态生成二级菜单
     - inclusion_tag 
     - 两层for循环 menu_dict.values()



### 动态生成二级菜单( 一级菜单排序 )

1. 登录成功保存权限信息和菜单信息到session中

   权限的数据结构：

   ​		permission_list = [  {  url  }]

   菜单的数据结构：

   ​		menu_dict = {  

   ​				一级菜单的ID： {  

   ​							title   icon   weight  children： [  {  url   title }  ]

   ​				 }

   ​		}

2. 中间件

   - 获取当前访问的url路径
   - 白名单
   - 登录状态的校验
   - 免认证的校验
   - 权限的校验
     - 从session中获取权限
     - 循环权限   正则匹配  

3. 模板

   - 母版和继承 
   - 动态生成二级菜单
     - inclusion_tag 
     - sorted  
     - 有序字典
     - 两层for循环 od.values()



### 动态生成二级菜单( 二级菜单默认选中 展开的状态 )

1. 登录成功保存权限信息和菜单信息到session中

   权限的数据结构：

   ​		permission_list = [  {  url  }]

   菜单的数据结构：

   ​		menu_dict = {  

   ​				一级菜单的ID： {  

   ​							title   icon   weight  children： [  {  url   title }  ]

   ​				 }

   ​		}

2. 中间件

   - 获取当前访问的url路径
   - 白名单
   - 登录状态的校验
   - 免认证的校验
   - 权限的校验
     - 从session中获取权限
     - 循环权限   正则匹配  

3. 模板

   - 母版和继承 
   - 动态生成二级菜单
     - inclusion_tag 
     - sorted  
     - 有序字典
     - 循环二级菜单
       - url  正则匹配
       - 匹配成功   二级菜单  class = active   一级菜单  class= ‘hide’ 移除
     - 两层for循环 od.values()



### 动态生成二级菜单(非菜单权限归属     访问子权限后者二级菜单 都让二级菜单选中 )

1. 登录成功保存权限信息和菜单信息到session中

   权限的数据结构：

   ​		permission_list = [  {  url  id  pid  }]

   菜单的数据结构：

   ​		menu_dict = {  

   ​				一级菜单的ID： {  

   ​							title   icon   weight  children： [  {  url   title  id }  ]

   ​				 }

   ​		}

2. 中间件

   - 获取当前访问的url路径

   - 白名单

   -  request.current_meni_id  = None

   - 登录状态的校验

   - 免认证的校验

   - 权限的校验

     - 从session中获取权限

     - 循环权限   正则匹配  

       - 获取id   pid 

       - 没有pid  当前访问的是二级菜单    request.current_meni_id = id

       - 有pid       当前访问的是子权限      request.current_meni_id = pid

         

3. 模板

   - 母版和继承 

   - 动态生成二级菜单

     - inclusion_tag 
     - sorted  
     - 有序字典
     - 循环二级菜单
       - request.current_meni_id    ==  二级菜单的id 
       - 匹配成功   二级菜单  class = active   一级菜单  class= ‘hide’ 移除
     - 两层for循环 od.values()

     

### 路径导航

1. 登录成功保存权限信息和菜单信息到session中

   权限的数据结构：

   ​		permission_dict = {   权限的id ：  {  url  id  pid   title }}

   菜单的数据结构：

   ​		menu_dict = {  

   ​				一级菜单的ID： {  

   ​							title   icon   weight  children： [  {  url   title  id }  ]

   ​				 }

   ​		}

2. 中间件

   - 获取当前访问的url路径

   - 白名单

   -  request.current_meni_id  = None

   - request.breadcrumb_list =   [  {  url： index   title ： 首页  } ]

   - 登录状态的校验

   - 免认证的校验

   - 权限的校验

     - 从session中获取权限   permission_dict

     - 循环权限   正则匹配  

       - 获取id   pid 

       - 没有pid  

         - 当前访问的是二级菜单  
           -   request.current_meni_id = id
           -   request.breadcrumb_list.append( {  url  i[url]   title  i[title]  }  )

       - 有pid       

         - 当前访问的是子权限     

           -  request.current_meni_id = pid
           - p_permisison = permission_dict[str(pid)]
           -  request.breadcrumb_list.append( {  url  p_permisison [url]   title  p_permisison [title]  }  )

           -  request.breadcrumb_list.append( {  url  i[url]   title  i[title]  }  )

3. 模板

   - 母版和继承 
   - 动态生成二级菜单
     - inclusion_tag 
     - sorted  
     - 有序字典
     - 循环二级菜单
       - request.current_meni_id    ==  二级菜单的id 
       - 匹配成功   二级菜单  class = active   一级菜单  class= ‘hide’ 移除
     - 两层for循环 od.values()

   - 路径导航
     - inclusion_tag 
     - 一层for循环 request.breadcrumb_list 

### 权限控制到按钮级别

1. 登录成功保存权限信息和菜单信息到session中

   权限的数据结构：

   ​		permission_dict = {   权限的name ：  {  url  id  pid   title  pname }}

   菜单的数据结构：

   ​		menu_dict = {  

   ​				一级菜单的ID： {  

   ​							title   icon   weight  children： [  {  url   title  id }  ]

   ​				 }

   ​		}

2. 中间件

   - 获取当前访问的url路径

   - 白名单

   -  request.current_meni_id  = None

   - request.breadcrumb_list =   [  {  url： index   title ： 首页  } ]

   - 登录状态的校验

   - 免认证的校验

   - 权限的校验

     - 从session中获取权限   permission_dict

     - 循环权限   正则匹配  

       - 获取id   pid   pname

       - 没有pid  

         - 当前访问的是二级菜单  
           -   request.current_meni_id = id
           -   request.breadcrumb_list.append( {  url  i[url]   title  i[title]  }  )

       - 有pid       

         - 当前访问的是子权限     

           -  request.current_meni_id = pid
           - p_permisison = permission_dict[pname]
           -  request.breadcrumb_list.append( {  url  p_permisison [url]   title  p_permisison [title]  }  )

           -  request.breadcrumb_list.append( {  url  i[url]   title  i[title]  }  )

3. 模板

   - 母版和继承 
   - 动态生成二级菜单
     - inclusion_tag 
     - sorted  
     - 有序字典
     - 循环二级菜单
       - request.current_meni_id    ==  二级菜单的id 
       - 匹配成功   二级菜单  class = active   一级菜单  class= ‘hide’ 移除
     - 两层for循环 od.values()

   - 路径导航
     - inclusion_tag 
     - 一层for循环 request.breadcrumb_list 

   - 权限控制到按钮级别
     - filter    -  has_permission
     - name  in  permission_dict    在返回True
     - {% if   request|has_permission: name   %}    { % endif %}

## 今日内容

1. 单个权限的新增编辑删除

2. 批量操作权限

   待新增的     路由系统中有  数据库中没有 

   待更新的     路由系统中有  数据库中也有 

   待删除的     路由系统中没有  数据库中有 

3. 分配权限

4. 权限组件的应用