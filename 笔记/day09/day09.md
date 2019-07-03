# day09

## 今日内容

- 三元运算
- 函数
- 考试题

## 内容详细

### 1. 三元运算（三目运算）

```python
v =  前面  if 条件 else 后面 

if 条件：
	v = '前面'
else:
    v = '后面'
```

```pytohn
# 让用户输入值，如果值是整数，则转换成整数，否则赋值为None

data = input('>>>')
value =  int(data) if data.isdecimal() else None 
```

注意：先做出来，再思考如何简化。

### 2. 函数

截至目前：面向过程编程。 【可读性差/可重用性差】。

```python
# 面向过程编程
user_input = input('请输入角色：')

if user_input == '管理员':
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('管理员，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["李邵奇", '15776556369@163.com'])
    msg['To'] = formataddr(["管理员", '344522251@qq.com'])
    msg['Subject'] = "情爱的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("15776556369@163.com", "qq1105400511")
    server.sendmail('15776556369@163.com', ['管理员', ], msg.as_string())
    server.quit()
elif user_input == '业务员':
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('业务员，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["李邵奇", '15776556369@163.com'])
    msg['To'] = formataddr(["业务员", '业务员'])
    msg['Subject'] = "情爱的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("15776556369@163.com", "qq1105400511")
    server.sendmail('15776556369@163.com', ['业务员', ], msg.as_string())
    server.quit()
elif user_input == '老板':
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('老板，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["李邵奇", '15776556369@163.com'])
    msg['To'] = formataddr(["老板", '老板邮箱'])
    msg['Subject'] = "情爱的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("15776556369@163.com", "qq1105400511")
    server.sendmail('15776556369@163.com', ['老板邮箱', ], msg.as_string())
    server.quit()
```

赠送：发送邮件

```python

```



函数式编程

```python

def send_email():
	import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('老板，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["李邵奇", '15776556369@163.com'])
    msg['To'] = formataddr(["老板", '老板邮箱'])
    msg['Subject'] = "情爱的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("15776556369@163.com", "qq1105400511")
    server.sendmail('15776556369@163.com', ['老板邮箱', ], msg.as_string())
    server.quit()


user_input = input('请输入角色：')

if user_input == '管理员':
    send_email()
elif user_input == '业务员':
    send_email()
elif user_input == '老板':
    send_email()
```

对于函数编程：

- 本质：将N行代码拿到别处并给他起个名字，以后通过名字就可以找到这段代码并执行。
- 场景：
  - 代码重复执行。
  - 代码量特别多超过一屏，可以选择通过函数进行代码的分割。

#### 2.1 函数的基本结构

```python
# 函数的定义
def 函数名():
    # 函数内容
    pass

# 函数的执行
函数名()
```

```python

def get_list_first_data():
    v = [11,22,33,44]
    print(v[0])


get_list_first_data()

# 注意：函数如果不被调用，则内部代码永远不会被执行。
```

```python
# 假如：管理员/业务员/老板用的是同一个邮箱。
def send_email():
	print('发送邮件成功，假设有10含代码')


user_input = input('请输入角色：')

if user_input == '管理员':
    send_email()
elif user_input == '业务员':
    send_email()
elif user_input == '老板':
    send_email()
```



#### 2.2 参数

```python

def get_list_first_data(aaa): # aaa叫形式参数(形参)
    v = [11,22,33,44]
    print(v[aaa])


get_list_first_data(1) # 2/2/1调用函数时传递叫：实际参数（实参）
get_list_first_data(2)
get_list_first_data(3)
get_list_first_data(0)
```

```python
# 假如：管理员/业务员/老板用的是同一个邮箱。
"""
def send_email(to):
	import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('导演，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["李邵奇", '15776556369@163.com'])
    msg['To'] = formataddr(["导演", to])
    msg['Subject'] = "情爱的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("15776556369@163.com", "qq1105400511")
    server.sendmail('15776556369@163.com', [to, ], msg.as_string())
    server.quit()
"""
def send_email(to):
    template = "要给%s发送邮件" %(to,)
    print(template)
 


user_input = input('请输入角色：')

if user_input == '管理员':
    send_email('xxxx@qq.com')
elif user_input == '业务员':
    send_email('xxxxo@qq.com')
elif user_input == '老板':
    send_email('xoxox@qq.com')
```

练习题

```python
# 1. 请写一个函数，函数计算列表 info = [11,22,33,44,55] 中所有元素的和。

def get_sum():
    info = [11,22,33,44,55]
    data = 0
    for item in info:
        data += item
    print(data)

get_sum()

# 2. 请写一个函数，函数计算列表中所有元素的和。

def get_list_sum(a1):
   	data = 0
    for item in a1:
        data += item
   	print(data)
    
get_list_sum([11,22,33])
get_list_sum([99,77,66])
v1 = [8712,123,123]
get_list_sum(v1)

# 3. 请写一个函数，函数将两个列表拼接起来。
def join_list(a1,a2):
    result = []
    result.extend(a1)
    result.extend(a2)
    print(result)
    
join_list([11,22,33],[55,66,77]

# 4. 计算一个列表的长度
def my_len(arg):
	count = 0
	for item in arg:
          count += 1
	print(count)

v = [11,22,33]
my_len(v)
len(v)

# 5. 发邮件的示例
          
def send_email(role,to):
    template = "要给%s%s发送邮件" %(role,to,)
    print(template)
 

user_input = input('请输入角色：')

if user_input == '管理员':
    send_email('管理员','xxxx@qq.com')
elif user_input == '业务员':
    send_email('业务员','xxxxo@qq.com')
elif user_input == '老板':
    send_email('老板','xoxox@qq.com')

```

#### 2.3 返回值

```python
def func(arg):
    # ....
    return 9 # 返回值为9 默认：return None

val = func('adsfadsf')
```

```python
# 1. 让用户输入一段字符串，计算字符串中有多少A字符的个数。有多少个就在文件a.txt中写多少个“李邵奇”。

def get_char_count(data):
    sum_counter = 0
    for i in data:
        if i == 'A':
            sum_counter += 1
            
	return sum_counter

def write_file(line):
    if len(line) == 0:
        return False  # 函数执行过程中，一旦遇到return，则停止函数的执行。
    with open('a.txt',mode='w',encoding='utf-8') as f:
        f.write(line)
	return True 


content = input('请输入:')
counter = get_char_count(content)
write_data = "李邵奇" * counter 
status = write_file(write_data)
if status:
    print('写入成功')
else:
    print('写入失败')

```

#### 2.4 上述总结

```python
# 情况1
def f1():
    pass 
f1()

# 情况2
def f2(a1):
    pass 
f2(123)

# 情况3
def f3():
    return 1 
v1 = f3()

# 情况4
def f4(a1,a2):
    # ... 
    return 999
v2 = f4(1,7)
```

#### 2.5 练习题

```python
# 1. 写函数，计算一个列表中有多少个数字，打印： 列表中有%s个数字。
#    提示：type('x') == int 判断是否是数字。
"""
# 方式一：
def get_list_counter1(data_list):
    count = 0
    for item in data_list:
        if type(item) == int:
            count += 1
	msg = "列表中有%s个数字" %(count,)
    print(msg)
    
get_list_counter1([1,22,3,'alex',8])

# 方式二：
def get_list_counter2(data_list):
    count = 0
    for item in data_list:
        if type(item) == int:
            count += 1
	return count
    
v = get_list_counter1([1,22,3,'alex',8])
msg = "列表中有%s个数字" %(v,)
print(msg)
"""

# 2. 写函数，计算一个列表中偶数索引位置的数据构造成另外一个列表，并返回。
"""
# 方式一：
def get_data_list1(arg):
    v = arg[::2]
    return v

data = get_data_list1([11,22,33,44,55,66])

# 方式二：
def get_data_list2(arg):
    v = []
    for i in range(0,len(arg)):
    	if i % 2 == 0:
    		v.append(arg[i])
   	return v

data = get_data_list2([11,22,33,44,55,66])

"""

# 3. 读取文件，将文件的内容构造成指定格式的数据，并返回。
"""
a.log文件
    alex|123|18
    eric|uiuf|19
    ...
目标结构：
a.  ["alex|123|18","eric|uiuf|19"] 并返回。
b. [['alex','123','18'],['eric','uiuf','19']]
c. [
	{'name':'alex','pwd':'123','age':'18'},
	{'name':'eric','pwd':'uiuf','age':'19'},
]
"""

```











