#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ################# 1. startswith / endswith
# name = 'alex'

# 判断是否已al开头
"""
# 方式一：
flag = name.startswith('al')
print(flag)
"""
"""
# 方式二：
val = name[0:2]
if val == 'al':
    print('是以al开头')
else:
    print('不是')
"""

# ################# 2. format
# name = "我叫{0},年龄:{1}".format('老男孩',73)
# print(name)

# ################# 3. encode
# name = '李杰' # 解释器读取到内存后，按照unicode编码存储：8个字节。
# v1 = name.encode('utf-8')
# print(v1)
# v2 = name.encode('gbk')
# print(v2)

# ################# 4. join
name = 'alex' # a_l_e_x
result = "**".join(name) # 循环每个元素，并在元素和元素之间加入连接符。
print(result)
