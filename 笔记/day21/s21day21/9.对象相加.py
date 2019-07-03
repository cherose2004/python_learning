#!/usr/bin/env python
# -*- coding:utf-8 -*-

val = 5 + 8
print(val)

val = "alex" + "sb"
print(val)

class Foo(object):
    def __add__(self, other):
        return 123

obj1 = Foo()
obj2 = Foo()
val  = obj1 + obj2
print(val)