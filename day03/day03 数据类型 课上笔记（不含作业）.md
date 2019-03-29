# day03

## 今日内容

1. 整型
2. 布尔类型
3. 字符串

## 内容回顾和补充

### 1. 内容回顾

作业：每周五写一个思维导图，罗列本周学习的知识点。

- xmind 软件
- processon 网站

### 2. 补充

1. 运算符补充

   - in

     ```
     value = "我是中国人"
     # 判断‘中国’是否在value所代指的字符串中。 “中国”是否是value所代指的字符串的子序列。
     v1 = "中国" in value
     
     # 示例
     content = input('请输入内容：')
     if "退钱" in content:
     	print('包含敏感字符')
     # 示例
     while True：
     	content = input('请输入内容：')
     	if "退钱" in content:
     		print('包含敏感字符')
     	else:
     		print(content)
     		break
     ```

   - not in

2. 优先级

   ```python
   not 2 > 1
   
   not 2     >    1   # 错误
   not    2>1   # 正确
   ```

### 3. 作业讲解

- 见代码：【1.三次登陆作业.py 】
- 见代码：【2..用户登陆三次并提示剩余次数.py】

### 4. pycharm自动生成头部代码

![1553822713745](C:\Users\oldboy-python\AppData\Roaming\Typora\typora-user-images\1553822713745.png)

![1553825155549](C:\Users\oldboy-python\AppData\Roaming\Typora\typora-user-images\1553825155549.png)



## 内容详细

### 1. 整型（int）

```python
age = 18
```

- py2

  - int

    - 32位电脑：-2147483648～2147483647
    - 64位电脑：-9223372036854775808～9223372036854775807
    - 超出范围后python自动将其转换成long（长整形）

  - 整型除法只能保留整数位。

    ```python
    from __future__ import division
    
    v = 9 /2
    print(v)
    ```

    

- py3

  - zhi有int
  - 整型除法只能保留所有。

### 2.  布尔值（bool/boolen）

- 只有两个值:True/False
- 转换
  - 数字转布尔：0是False，其他都是True
  - 字符串转布尔：“”是False，其他都是True

### 3.  字符串（str/string）

- 字符串特有
  - .upper()  /  .lower()
  - .isdigit()
  - .strip()  / .lstrip()  / .rstrip()
  - .replace("被替换的字符/子序列","要替换为的内容")  /  .replace("被替换的字符/子序列","要替换为的内容", 1)
  - .split('根据什么东西进行分割') /  .split('根据什么东西进行分割', 1 )  / rsplit 

- 公共

  - len ，计算长度。 （字符串->计算字符串中的字符个数）

  - 索引取值（0作为开始）

    ```python
    v = "oldboy"
    v1 = v[0]  # 0 1 2 3 ... 从前向后
    v2 = v[-1] # -1 -2 -3 ...从后向前
    ```

  - 切片（0作为开始）

    ```python
    v = "oldboy"
    
    # v1 = v[2:4] #   2 =< 索引位置 <3
    # v2 = v[3:6]
    # v2 = v[3:-1]
    # v2 = v[3:]
    # v2 = v[:-1]
    # print(v2)
    
    # 示例: 取最后两个字符
    # data = input('请输入：')
    # 方式一
    # v = data[-2:]
    # print(v)
    # 方式二
    # total_len = len(data)
    # v = data[total_len-2:total_len]
    # print(v)
    ```

    

- 练习题

  ```python
  """
  需求：让用户输入任意字符串，获取字符串之后并计算其中有多少个数字。
  """
  """
  total = 0
  text = input('请输入内容：') # ads2kjf5adja453421sdfsdf
  index_len = len(text)
  index = 0
  while True:
      val = text[index]
      #print(val) # "a"
      # 判断val是否是数字
      #     - 是数字：total + 1
      #     -   不是：继续玩下走，执行下一次循环去检查下一个字符。
      flag = val.isdigit()
      if flag:
          total = total + 1 # total += 1
      if index == index_len - 1:
          break
      index += 1
  
  print(total)
  """
  ```

  

