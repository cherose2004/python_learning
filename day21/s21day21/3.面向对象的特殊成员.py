#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
py文件的注释
"""

"""
class Foo:
    def __init__(self,a1):
        self.a1 = a1

# 1.创建一个空对象 obj 
# 2.执行 __init__ ，给对象中进行赋值（初始化） 对象.a1 = alex 
obj = Foo('alex')
"""
class Foo(object):
    def __call__(self, *args, **kwargs):
        print('执行call方法')

# obj = Foo()
# obj()
Foo()()


