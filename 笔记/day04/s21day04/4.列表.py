#!/usr/bin/env python
# -*- coding:utf-8 -*-

# #################################### 公共功能 #########################################
# 1. for循环
"""
users = ['李邵奇','利奇航','张三丰','李子森']
for i in users:
    print(i)
"""
"""
users = ['李邵奇','利奇航','张三丰','李子森']
for i in users:
    # 第一次循环：i=“李邵奇”
    print(i)
    for ele in i:
        print(ele)
"""

# 练习题：请通过for循环和数字计数器实现：users = ['李邵奇','利奇航','张三丰','李子森']
"""
    0 李邵奇
    1 利奇航
    2 张三丰
    3 李子森
"""
"""
# 方式一
users = ['李邵奇','利奇航','张三丰','李子森']
count = 0
for i in users:
    print(count,i)
    count += 1
"""
"""
# 方式二
users = ['李邵奇','利奇航','张三丰','李子森']
users_len = len(users) # 4
for index in range(0,users_len): # [0,1,2,3]
    print(index,users[index])
"""

# #################################### 独有功能 #########################################

# 1. 列表的最后追加一个元素
# users = []
# users.append('alex')
# print(users)
"""
示例一：
users = []
while True:
    name = input('请输入姓名:')
    users.append(name)
    print(users)
"""
"""
示例二：
# 录入用户和密码
users = []
for i in range(0,3):
    name = input('请输入用户名和密码:')
    users.append(name)
print(users) # ['alex,123', 'oldboy,888', 'lishaoqi,123']

# 用户和密码校验
username = input('请输入要登陆用户名：')
password = input('请输入要登陆密码：')
for item in users:
    result = item.split(',') # ['alex','123']
    user = result[0]
    pwd = result[1]
    if user == username and pwd == password:
        print('登陆成功')
        break
        
"""


# 2. insert , 在指定索引位置进行插入元素
"""
users = ['李邵奇','利奇航','张三丰','李子森']
users.insert(1,'小黑')
print(users)
"""
# 3. remove

# users = ['李邵奇','张三丰','利奇航','张三丰','李子森']
# users.remove('张三丰')
# print(users)

# 4. pop
# users = ['李邵奇','张三丰','利奇航','张三丰','李子森']
# # users.pop(2)
# users.pop() # 默认删除最后一个
# print(users)

# 5. clear
# users = ['李邵奇','张三丰','利奇航','张三丰','李子森']
# users.clear()
# print(users)



"""
users = ['李邵奇','张三丰','利奇航','张三丰','李子森']
del users[1]
print(users)
"""












