#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo:
    def __init__(self,name):
        self.__x = name


obj = Foo('alex')

print(obj._Foo__x) # 强制访问私有实例变量



