## 内容回顾

### cookie

#### 定义

保存在浏览器上的一组组键值对。

#### 为什么有cookie？

http协议是无状态的。每次http请求都是对立的，相互之间没有关联。用cookie保存状态。

#### 特性

1. 由服务器让浏览器进行设置的。
2. 浏览器保存在浏览器本地上。
3. 下次访问时会自动携带相应的cookie

#### django中操作cookie

​	1.设置   本质   set-cookie ： ‘key:value’

​	ret =  HttpResponse('xxxxx')

​	ret.set_cookie(key ,  value , max_age=1000,path='/')      domain  secure   httponly 

​    ret.set_signed_cookie(key ,  value ,  salt='s21'   )

2. 获取   本质 cookie ： ‘’

   request.COOKIES   []   get()

   request.get_signed_cookie(key,salt='s21',default='xx')

3. 删除     set-cookie ： ‘key:"" ,max-age=0’

   ret =  HttpResponse('xxxxx')

   ret.delete_cookie(key)

   

### session

#### 定义

保存在服务器上的一组组键值对,必须依赖cookie

#### 为什么要有session？

1. cookie保存在浏览器本地，不安全
2. cookie的大小受到限制

#### django中操作session

1.设置：

request.session[key] = value

2.获取

request.session[key]       request.session.get(key)

3.删除

del request.session[key]     request.session.pop(key)

request.session.delete()   #  删除session的数据   不删除cookie

request.session.flush()      #  删除session的数据   删除cookie

4.其他

request.session.session_key

request.session.set_expiry(value)

request.session.clear_expiried()

5.配置

存放session的位置   db  

SESSION_SAVE_EVERY_REQUEST = False

from django.conf import global_settings

## 今天内容

### 1.csrf装饰器

```
from django.views.decorators.csrf import csrf_exempt,csrf_protect，ensure_csrf_cookie
csrf_exempt   某个视图不需要进行csrf校验
csrf_protect  某个视图需要进行csrf校验
ensure_csrf_cookie  确保生成csrf的cookie
```

### 2.csrf功能

1.csrf中间件中执行process_request：

​	1. 从cookie中获取到csrftoken的值

	2. csrftoken的值放入到 request.META

2.执行process_view

 1. 查询视图函数是否使用csrf_exempt装饰器，使用了就不进行csrf的校验

 2. 判断请求方式：

     1. 如果是GET', 'HEAD', 'OPTIONS', 'TRACE'

        不进行csrf校验

    	2. 其他的请求方式（post，put）

        进行csrf校验：

        1.获取cookie中csrftoken的值

        获取csrfmiddlewaretoken的值

        ​	能获取到  ——》 request_csrf_token

        ​	获取不到   ——》 获取请求头中X-csrftoken的值 ——》request_csrf_token

        比较上述request_csrf_token和cookie中csrftoken的值，比较成功接收请求，比较不成功拒绝请求。

### 3.ajax

<https://www.cnblogs.com/maple-shaw/articles/9524153.html>

#### 1.发请求的方式

1.地址栏输入地址  GET

2.form表单  GET/POST  

3.a标签   GET

#### 2.ajax 

就是使用js的技术发请求和接收响应的。

特点：

1. 异步
2. 局部刷新
3. 传输的数据量少

#### 3.jqery发ajax请求

```
$.ajax({
    url: '/calc/',
    type: 'post',
    data: {
        a: $("[name='i1']").val(),
        b: $("[name='i2']").val(),
    },
    success: function (res) {
        $("[name='i3']").val(res)
    },
    error:function (error) {
        console.log(error)
    }
})
```

#### 4.上传文件：

```html
<input type="file" id="f1">
<button id="b1">上传</button>


$('#b1').click(function () {
        var  formobj =  new FormData();

        formobj.append('file',document.getElementById('f1').files[0]);
        // formobj.append('file',$('#f1')[0].files[0]);
        formobj.append('name','alex');

        $.ajax({
            url: '/upload/',
            type: 'post',
            data:formobj ,
            processData:false,  // 
            contentType:false,
            success: function (res) {
                $("[name='i3']").val(res)
            },
        })
    })
```

#### 5.ajax通过csrf的校验：

前提条件：确保有csrftoken的cookie

在页面中使用{% csrf_token %}

加装饰器 ensure_csrf_cookie

from django.views.decorators.csrf import csrf_exempt,csrf_protect,  ensure_csrf_cookie

1.给data中添加csrfmiddlewaretoken的值

```html
data: {
    'csrfmiddlewaretoken':$('[name="csrfmiddlewaretoken"]').val(),
    a: $("[name='i1']").val(),
    b: $("[name='i2']").val(),
},
```

2.加请求头

```html
headers:{
    'x-csrftoken':$('[name="csrfmiddlewaretoken"]').val(),
},
```

3.使用文件

同方式2