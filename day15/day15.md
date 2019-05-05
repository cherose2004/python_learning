# day15

## 今日内容

- 模块知识
- 内置模块
  - time
  - datetime
  - json
  - 其他

## 内容回顾 & 作业题

重要知识点

- 构造字典和函数对应关系，避免重复的if else
- a=1 b=2 ==>  a,b = b,a 
- 装饰器
- 找文件路径
- 脚本参数
- sys.exit
- range / xrange 
- 读大文件
- 面试题如果遇到有歧义，一定要给出多种情况。



## 今日内容

### 1.模块基本知识

- 内置模块，python内部提供的功能。

  ```
  import sys
  print(sys.argv)
  ```

- 第三方模块，下载/安装/使用。

  ```
  # 把pip.exe 所在的目录添加到环境变量中。
  
  pip install 要安装的模块名称  # pip install xlrd
  ```

  - 网慢
    ![1555473193871](C:\Users\oldboy-python\AppData\Roaming\Typora\typora-user-images\1555473193871.png)

  - python36  -m pip install --upgrade pip

    ![1555473313857](C:\Users\oldboy-python\AppData\Roaming\Typora\typora-user-images\1555473313857.png)
    ![1555473548105](C:\Users\oldboy-python\AppData\Roaming\Typora\typora-user-images\1555473548105.png)

  - 安装完成后，如果导入不成功。

    - 重启pycharm。
    - 安装错了。

- 自定义模块

  - xxxx.py

    ```python
    def f1():
        print('f1')
    
    
    def f2():
        print('f2')
    ```

  - x1.py

    ```python
    # 调用自定义模块中的功能
    import xxxx
    xxxx.f1()
    xxxx.f2()
    ```

  - 运行

    ```
    python x1.py 
    ```

### 2.内置模块

#### 2.1 os

- os.makedirs，创建目录和子目录

  ```
  import os
  file_path = r'db\xx\xo\xxxxx.txt'
  
  file_folder = os.path.dirname(file_path)
  if not os.path.exists(file_folder):
      os.makedirs(file_folder)
  
  with open(file_path,mode='w',encoding='utf-8') as f:
      f.write('asdf')
  ```

- os.rename，重命名

  ```
  import os
  os.rename('db','sb')
  ```

- os.path.join

- os.path.dirname

- os.path.abspath

- os.path.exists

- os.stat('文件路径')

- os.listdir

- os.walk

#### 2.2 sys

- sys.argv 

- sys.path ，默认Python去导入模块时，会按照sys.path中的路径挨个查找。 

  ```
  # import sys
  # sys.path.append('D:\\')
  # import oldboy
  ```

- sys是解释器相关的数据：递归次数/引用次数

#### 2.3 json

json是一个特殊的字符串。 【长的像列表/字典/字符串/数字/真假】

```
import json
# 序列化，将python的值转换为json格式的字符串。
# v = [12,3,4,{'k1':'v1'},True,'asdf']
# v1 = json.dumps(v)
# print(v1)

# 反序列化，将json格式的字符串转换成python的数据类型
# v2 = '["alex",123]'
# print(type(v2))
# v3 = json.loads(v2)
# print(v3,type(v3))
```

```
    +-------------------+---------------+
    | Python            | JSON          |
    +===================+===============+
    | dict              | object        |
    +-------------------+---------------+
    | list, tuple       | array         |
    +-------------------+---------------+
    | str               | string        |
    +-------------------+---------------+
    | int, float        | number        |
    +-------------------+---------------+
    | True              | true          |
    +-------------------+---------------+
    | False             | false         |
    +-------------------+---------------+
    | None              | null          |
    +-------------------+---------------+
```

