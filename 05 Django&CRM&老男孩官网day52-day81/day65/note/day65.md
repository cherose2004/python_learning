## 内容回顾

### json

一种数据交换的格式

python

支持的数据类型：字符串、数字、列表、字典、布尔值、None

转化：序列化   josn.dumps(python的数据)      josn.dump(python的数据,f)    

​	      反序列化   josn.loads(json的字符串)      josn.load(json的字符串,f)

js

支持的数据类型：字符串、数字、数组、对象、布尔值、null

转化：

序列化：JSON.stringfy(js的数据类型)

反序列化：JSON.parse(json的字符串)

```
from django.http.response import JsonResponse
```

### 发请求的方式

1.在地址栏种输入地址   GET

2.a标签    GET

3.form表单   GET/POST

	1. method   请求方式  action  地址
 	2. 标签要有name属性   有的需要有value
 	3. 要有一个input  type=‘submit’  或者button

### ajax

使用js发送请求。

特点：异步  局部刷新 传输的数据量小

#### 使用

jq发ajax 

导入jq

$.ajax({

​		url：发送的地址，

​		type:   请求方式，

​		data:  {},   

​		successs: funcation(res){    res  ——>响应体

​		}

})

#### 上传文件

var   formobj  = new FormData()

formobj.append(key,  $("#f1")[0].files[0] )

$.ajax({

​		url：发送的地址，

​		type:   请求方式，

​		processData: false;    // 不处理编码方式

​		contentType:false;    //  不处理请求头

​		data: formobj ,   

​		successs: funcation(res){    res  ——>响应体

​		}

})

#### ajax通过django的csrf校验

1.给data添加csrfmiddlewaretoken的键值对

```html
dada:{
	'csrfmiddlewaretoken':  隐藏的input的值   cookie中csrftoken的值
}
```

2.添加请求头

hearders:{
	'x-csrftoken':  隐藏的input的值   cookie中csrftoken的值
}

3.文件导入

## 今日内容

### from组件

#### form组件的功能

1. 生产input标签
2. 对提交的数据可以进行校验
3. 提供错误提示

#### 定义form组件

```python
from django import forms


class RegForm(forms.Form):
    username = forms.CharField()
    pwd = forms.CharField()
```

#### 使用

视图

```python
form_obj = RegForm()
form_obj = RegForm(request.POST)
form_obj.is_valid():  # 对数据进行校验
print(form_obj.cleaned_data)  # 通过校验的数据

return render(request, 'reg2.html', {'form_obj': form_obj})
```

模板

```
{{ form_obj.as_p }}    __>   生产一个个P标签  input  label
{{ form_obj.errors }}    ——》   form表单中所有字段的错误
{{ form_obj.username }}     ——》 一个字段对应的input框
{{ form_obj.username.label }}    ——》  该字段的中午提示
{{ form_obj.username.id_for_label }}    ——》 该字段input框的id
{{ form_obj.username.errors }}   ——》 该字段的所有的错误
{{ form_obj.username.errors.0 }}   ——》 该字段的第一个错误的错误

```

#### 常用字段

```
CharField    
ChoiceField 
MultipleChoiceField  
```

#### 字段参数

```
required=True,               是否允许为空
widget=None,                 HTML插件
label=None,                  用于生成Label标签或显示内容
initial=None,                初始值
error_messages=None,         错误信息 {'required': '不能为空', 'invalid': '格式错误'}
validators=[],               自定义验证规则
disabled=False,              是否可以编辑
```

#### 验证

##### 1.内置校验

```
required=True
min_length
max_length
```

##### 2.自定义校验器

1. 写函数

```
def checkname(value):
    # 通过校验规则 不做任何操作
    # 不通过校验规则   抛出异常
    if 'alex' in value:
        raise ValidationError('不符合社会主义核心价值观')
```

2.使用内置的校验器

```
from django.core.validators import RegexValidator
```

##### 3.钩子函数：

1. 局部钩子

   ```
   def clean_字段名(self):
       # 局部钩子
       # 通过校验规则  必须返回当前字段的值
       # 不通过校验规则   抛出异常
       raise ValidationError('不符合社会主义核心价值观')
   ```

2. 全局钩子

   ```
   def clean(self):
       # 全局钩子
       # 通过校验规则  必须返回当前所有字段的值
       # 不通过校验规则   抛出异常   '__all__'
       pass
   ```

#### is_valid的流程：

1.执行full_clean()的方法：

定义错误字典

定义存放清洗数据的字典

2.执行_clean_fields方法：

​	循环所有的字段

​	获取当前的值

​    对进行校验 （ 内置校验规则   自定义校验器）

 1. 通过校验

    self.cleaned_data[name] = value 

    如果有局部钩子，执行进行校验：

    通过校验——》 self.cleaned_data[name] = value 

    不通过校验——》     self._errors  添加当前字段的错误 并且 self.cleaned_data中当前字段的值删除掉

	2. 没有通过校验

    self._errors  添加当前字段的错误

3.执行全局钩子clean方法

