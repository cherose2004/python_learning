## 内容回顾

web开发中 一个url代表一个权限

表结构设计

权限表

id   

url   权限    url地址正则表达式    不带^ $

title   标题 



角色表

id  

name   角色的名称

permissions  多对多    权限



用户表

id 

username  用户名

password  密码

roles    多对多   角色



用户和角色关系表

id   

user_id

role_id 



角色和权限的关系表

id 

role_id 

permission_id 

1.流程

1. 登录

- 中间件
  - 白名单
- 登录成功
  - 查询到该用户的权限信息
  - 把权限信息、登录状态保存到session中   

2. 中间件
   - 获取当前访问的URL
   - 白名单
   - 登录状态的校验
   - 免认证地址的校验
   - 权限的校验
     - 从session中获取到权限的信息
     - 循环权限，拿到权限url   和当前的url正则匹配
       - 匹配成功  有权限 
       - 都没有匹配成功  没有权限 返回拒绝的信息



今日内容：

1.补充git 

版本控制

git init  

配置

git config  -- global  user

git config  -- global  email

git add 文件 

git add .  

git  commit -m  '描述'

git log   

git reflog   

git reset --hard   

git status



git remote add  origin 'url'

git push origin  master 

git pull  origin master 

git clone  url 



分支

git branch 查看分支

git branch dev  创建dev分支

git checkout dev    切换分支

git merge dev    合并分支

git branch -d debug  删除分支



个人开发的流程

分支  master  dev

开发时在dev上开发 

写完新的功能 合并到master上

出现bug：

	1. 创建debug分支
 	2. 切换到debug分支，修改bug
 	3. 修改完成后提交，切换到master，合并debug的分支
 	4. 切换到dev分支 合并master/debug分支
 	5. 删除debug的分支

注意：合并分支有冲突，手动解决冲突



团队合作开发

分支  master dev  star  maple

每个人在自己的分支上操作

开发完功能 本地代码推送到自己的分支上

创建pull request 合并到dev上

领导审核代码  接收合并

dev  ——》 master

1.动态生成一级菜单

2.动态生成二级菜单










