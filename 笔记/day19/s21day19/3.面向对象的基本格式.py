#!/usr/bin/env python
# -*- coding:utf-8 -*-

# # 函数
# def func():
#     pass

# 定义一个类：Account
class Account:
    # 方法
    def login(self,name):
        print('登陆')
        return 123

    def logout(self):
        print('注销')


# 调用类中的方法
# 1.创建对象
x = Account() # 创建了一个Account类的对象
# 2.使用对象调用类中的方法
val = x.login('alex')
print(val)
