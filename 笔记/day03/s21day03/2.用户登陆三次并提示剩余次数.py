#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
此文件是用于给同学演示用户三次登陆的示例
"""



# ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）

# 功能一：用户登陆
"""
user = input('请输入用户名:')
pwd = input('请输入密码:')
if user == 'oldboy' and pwd == 'alex':
    print('登陆成功')
else:
    print('登陆失败')
"""

# 功能二：三次机会并提示
"""
count = 1
while count <= 3:
    x = input('请输入：')
    # print('用户名和密码输入和校验，错误')
    # print(count) # 剩余2次/ 1次/ 0次
    timer = 3 - count
    template = "用户名或密码输入错误，剩余%s次机会。" %(timer,)
    print(template)
    count += 1
"""
"""
count = 2
while count >=0:
    user = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user == 'oldboy' and pwd == 'alex':
        print('欢迎登陆')
        break
    else:
        template = "用户名或密码输入错误，剩余%s次机会。" % (count,)
        print(template)
    count -= 1
"""

count = 2
while count >=0:
    user = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user == 'oldboy' and pwd == 'alex':
        print('欢迎登陆')
        break
    template = "用户名或密码输入错误，剩余%s次机会。" % (count,)
    print(template)
    count -= 1
else:
    print('三次机会用完')