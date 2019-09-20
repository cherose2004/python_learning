#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo(object):
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

obj = Foo('alex',19,'xxxx@qq.com')
print(obj)
print(obj.name)
print(obj.age)
print(obj.email)
val = obj.__dict__ # 去对象中找到所有变量并将其转换为字典
print(val)
