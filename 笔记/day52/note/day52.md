内容概要

1.web框架的本质

2.django的下载安装使用

# 内容回顾

python基础

面向对象

网络编程

并发编程

数据库

前端

### tcp/ip五层模型

应用层

传输层

网络层

数据链路层

物理层

![1560214235629](asset\1560214235629.png)

### socket 

 套接字  位于应用层和传输层之间的虚拟层  一组接口

c/s    ——》   b/s 

百度的服务器   socket服务端

1. 创建socket服务端
2. 绑定IP和端口
3. 监听
4. 等待链接

7. 接收数据
8. 返回数据
9. 断开链接

浏览器   socket客户端

5. 链接服务端
6. 发送数据

9. 接收数据
10. 断开链接



web框架   —— 》  socket服务端 

![1560219121217](asset\1560219121217.png)



### HTTP协议

请求和应答 应用层协议

#### 状态码

1xx   

2xx

3xx  重定向

4xx  请求的错误

5xx  服务器的错误

#### 请求方式  8种

get    ——》 获取一个页面、图片（资源）

post ——》 提交数据

#### url

http://www.cnblogs.com/maple-shaw/articles/9060408.html

协议  域名和端口  HTTP（80） HTTPS(443)    路径   参数 

#### 请求（request）

浏览器  —— 》 服务器  

GET 请求没有请求数据

“请求方式 url路径 协议版本\r\n

k1:v1\r\n

k2:v2\r\n

\r\n

数据”

#### 响应（response）

服务器  —— 》 浏览器 

“协议版本 状态码 状态码描述\r\n

k1:v1\r\n

k2:v2\r\n

\r\n

响应数据（响应体）”

#### web框架的功能

1.socket收发消息    - wsgiref   uwsgi 

2.根据不同的路径返回不同的内容

3.返回动态页面（字符串的替换） —— jinja2



django

2 3 

flask 

2

tornado

1 2 3 



### django

#### 下载安装

1.命令行

pip3 install django==1.11.21 -i https://pypi.tuna.tsinghua.edu.cn/simple

2.pycharm

#### 创建项目

1.命令行：

找一个文件夹存放项目文件：

打开终端：

django-admin startproject 项目名称

项目目录

![1560226751493](asset\1560226751493.png)

2.pycahrm

![1560227015628](asset\1560227015628.png)

#### 启动

1.命令行

切换到项目的根目录下  manage.py

`python36 manage.py runserver `  —— <http://127.0.0.1:8000/>

`python36 manage.py runserver 80 `   在80端口启动

`python36 manage.py runserver 0.0.0.0:80`   0.0.0.0:80

2.pycharm

点绿三角启动 可配置

#### 简单使用

模板 ——》HTML  指定文件夹

urls.py

```python
# 导入
from django.shortcuts import HttpResponse,render

# 函数
def index(request):
    # return HttpResponse('index')
    return render(request,'index.html')

# url和函数对应关系
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
]
```

















