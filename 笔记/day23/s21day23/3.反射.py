#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo(object):
    def get(self):
        pass

obj = Foo()
# if hasattr(obj,'post'):
#     getattr(obj,'post')

v1 = getattr(obj,'get',None) # 推荐
print(v1)