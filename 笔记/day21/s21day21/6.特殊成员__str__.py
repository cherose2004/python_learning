#!/usr/bin/env python
# -*- coding:utf-8 -*-

# v = "asdfasdf"
# print(v)
#
# class Foo(object):
#     def __str__(self):
#         """
#         只有在打印对象时，会自动化调用此方法，并将其返回值在页面显示出来
#         :return:
#         """
#         return 'asdfasudfasdfsad'
#
# obj = Foo()
# print(obj,type(obj))

class User(object):
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def __str__(self):
        return "%s %s" %(self.name,self.email,)
user_list = [User('二狗','2g@qq.com'),User('二蛋','2d@qq.com'),User('狗蛋','xx@qq.com')]
for item in user_list:
    print(item)