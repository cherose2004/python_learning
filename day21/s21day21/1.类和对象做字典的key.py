#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Foo(object):
    pass

obj1 = Foo() # v = 123
obj2 = Foo() # v = 456

info = {'1':1, Foo:123,obj1:111,obj2:222}
print(info)
print(info[Foo])