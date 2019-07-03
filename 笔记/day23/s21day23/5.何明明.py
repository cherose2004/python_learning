#!/usr/bin/env python
# -*- coding:utf-8 -*-
class User(object):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

obj = User('何明明','xxx@qq.com',84)
print(obj.name)
