#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""



"""
需求：用户三次登陆

1. 功能拆分
2. 拼凑功能（中文）
"""

# 功能一：用户登陆
"""
user = input('请输入用户名:')
pwd = input('请输入密码:')
if user == 'oldboy' and pwd == 'alex':
    print('登陆成功')
else:
    print('登陆失败')
"""
# 功能二：三次机会
"""
count = 1
while count <= 3:
    print(count)
    count += 1
"""

# ########################### 功能嵌套 #################################
"""
count = 1
while count <= 3:
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    if user == 'oldboy' and pwd == 'alex':
        print('登陆成功')
        break
    else:
        print('登陆失败')
    if count == 3:
        break
    count += 1
"""

"""
需求：用户三次登陆,允许用户最多尝试3次，每尝试3次后，如果还没输入正确，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。

1. 功能拆分
2. 拼凑功能（中文）
"""

count = 1
while count <= 3:
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    if user == 'oldboy' and pwd == 'alex':
        print('登陆成功')
        break
    else:
        print('登陆失败')
    if count == 3:
        choice = input('请输入是否继续（Y/N）：')
        if choice == 'N':
            break
        elif choice == 'Y':
            count = 1
            continue
        else:
            print('输入错误')
            break
    count += 1