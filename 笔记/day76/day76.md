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



1. 拷贝rbac组件到新项目中，并注册

   ```
   INSTALLED_APPS = [
   		...
       'rbac.apps.RbacConfig'
   ]
   ```

2. 数据库迁移

   1. 修改用户表

      ```python
      class User(models.Model):
          """用户表"""
          # username = models.CharField('用户名', max_length=32)
          # password = models.CharField('密码', max_length=32)
          roles = models.ManyToManyField(Role, verbose_name='用户所拥有的角色', blank=True)
      	# 多对多关联写成类  不写字符串
          class Meta:
              abstract = True  # 数据库迁移时不生成表  作基类 继承使用
      ```

   2.  新项目的用户表继承User

      ```python
      from rbac.models import User
      class UserProfile(User):
      ```

   3. 执行数据库迁移的命令

      1. 先删除rbac中migrations中的除了init之外的py文件

      2. 执行 

         python manage.py makemigrations

         python manage.py migrate

3. 路由配置

   ```
   urlpatterns = [
    	....
       url(r'^rbac/', include('rbac.urls')),
   ]
   ```

4. 角色管理

   <http://127.0.0.1:8000/rbac/role/list/>

5. 一级菜单管理

   <http://127.0.0.1:8000/rbac/menu/list/>

6. 批量操作权限

   <http://127.0.0.1:8000/rbac/multi/permissions/>

   批量输入标题

   给权限分配给一级菜单  给父权限分配子权限

7. 分配权限

   如果用的不是rbac的User，替换User为当前使用的用户model

   给角色分权限

   给用户分角色

8. 应用权限的中间件

   ```
   MIDDLEWARE = [
   	...
       'rbac.middlewares.middleware.AuthMiddleWare',
   
   ]
   ```

   在settings中添加权限的配置

   ```
   #  白名单
   WHITE_LIST = [
       r'/login/$',
       r'/reg/$',
       r'/admin/.*'
   ]
   
   # 免认证的地址
   NO_PERMISSION_LIST = [
       r'/index/'
   
   ]
   
   # 权限的session的key
   PERMISSION_SESSION_KEY = 'permission'
   
   # 菜单的session的key
   MENU_SESSION_KEY = 'menu'
   ```

   登录成功后调用权限信息初始化的函数

9. 动态生成二级菜单

   ```
   {% load rbac %}
   {% menu request %}
   ```

​	使用 css js

​	<link rel="stylesheet" href="{% static 'css/nav.css' %} "/>

	<script src="{% static 'rbac/js/menu.js' %} "></script>

10. 路径导航

    ```
    {% breadcrumb request %}
    ```

11. 权限控制到按钮级别

    ```
    {% load rbac %}
    
    
    {% if request|has_permission:'add_consult' %}
           <a href="{% url 'add_consult' customer_id %}" class="btn btn-primary">新增</a>
    {% endif %}
    ```