# day05  数据类型

## 今日内容

- 字典

## 作业题讲解和变换

见：代码文件



## 内容回顾和补充

- int

  - py2/py3 
  - 除法
  - 强制转换：
    - int('字符串')  【重要】
    - int(布尔值)

- bool

  - 强制转换：

    - bool(整数)       ->    bool(1)/..                             -> bool(0)

    - bool(字符串)    ->   bool('xx')                             --> bool("")

    - bool(列表)        ->  bool([])                                 --> bool([])

    - bool(元组)        -> bool(())                                 --> bool(空元组)

      ```python
      v1 = bool(0)
      v2 = bool("")
      v3 = bool([])
      v4 = bool(())
      print(v1,v2,v3,v4) # False
      ```

- str

  - 独有功能：upper/lower/split/strip/replace/isdigit/startswith/endswith/format/join/encode
  - 公共公共：
    - len
    - 索引
    - 切片
    - 步长
    - for循环
    - 删除【无】
    - 更新【无】
  - 强制转换：
    - str(999)  # "999"
    - str(True) # "True"
    - str(["唐开发",'李忠伟'])   #  "["唐开发",'李忠伟']"   -->   v2 = "".join(["唐开发",'李忠伟'])
    - str(["唐开发",'李忠伟']) 

- list

  - 独有功能：append/insert/pop/remove/clear/ extend 

  - 公共功能：

    - len
    - 索引
    - 切片
    - 步长
    - for循环
    - 删除
    - 更新

  - 强制转换：

    - list("asdfadfasfdadfasfd")

      ```python
      v1 = list("asdfadfasfdadfasfd")
      print(v1)
      ```

    - list( (11,22,33,44,) )

      ```python
      v1 = list( (11,22,33,44,) )
      print(v1)
      ```

- tuple

  - 独有功能【无】

  - 公共功能：

    - len
    - 索引
    - 切片
    - 步长
    - for循环
    - 删除【无】
    - 更新【无】

  - 强制转换：

    - tuple('adfadfasdfasdfasdfafd')

      ```python
      v1 = tuple('adfadfasdfasdfasdfafd')
      print(v1)
      ```

    - tuple([11,22,33,44])

      ```python
      v1 = tuple([11,22,33,44])
      print(v1)
      ```

- 总结

  - 常见的类型转换

    ```python
    # 字符串转数字
    
    # 数字转字符串
    
    # 列表转元组
    
    # 元组转列表
    
    # 其他转bool时，只有：0 “”  []  () 
    ```

    ```python
    # 练习题
    nums = [11,22,33,44]
    for i in range(0,len(nums)):
        nums[i] = str(nums[i])
    resutl = '_'.join(nums)
    print(resutl)
    
    # 1. "".jon([元素必须是字符串,元素必须是字符串,])
    ```



## 今日内容

### 1. 字典

帮助用户去表示一个事物的信息（事物是有多个属性）。

```python
info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'} # 键值

# 请输出：我今天点%s,他的年龄是%s,性别是%s，他喜欢他的%s;
```

基本格式

```python
data = {键:值,键:值,键:值,键:值,键:值,键:值,}
```

```python
# 练习题
userinfo = {'usenrame':'alex','password':"oldboy"}

user = input('请输入用户：')
pwd = input('请输入密码：')

if userinfo['username'] == user and userinfo['password'] == pwd:
    print('登陆成功')
else:
    print('用户名或密码错误')



```

1. 独有功能

   ```python
   info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
   ```

   - keys，获取字典中所有的键。     ['name','age','gender','hobby']

     ```python
     # for item in info.keys():
     #     print(item)
     ```

   - values，获取字典中所有的值。  ['刘伟达','18','男','同桌']

     ```python
     # for item in info.values():
     #     print(item)
     ```

   - items，获取字典中的所有键值对。

     ```python
     # for v1,v2 in info.items():
     #     print(v1,v2)
     ```

2. 公共功能

   - len

     ```
     info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
     print(len(info))
     ```

   - 索引

     ```
     info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
     info['name']
     info['age']
     ```

   - 切片【无】

   - 步长【无】

   - for

     ```
     info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
     
     for item in info.keys():
         print(item)
     
     for item in info.values():
         print(item)
     
     for k,v in info.items():
         print(k,v)
     ```

   - 修改（存在就修改/不存在就增加）

     ```python
     # 改值
     info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
     info['age'] = 19
     print(info)
     
     # 改键
     # 删除后再增加
     del info['hobby']
     info['xxxxx'] = 'x1'
     ```

   - 删除

     ```python
     info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
     
     del info['name']
     print(info)
     
     ```

     

## 重点

- int
- bool
- str
- list
- tuple
- dict



