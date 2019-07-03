#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo:
    city = '北京'

    def __init__(self, name):
        self.name = name

    def func(self):
        pass


obj1 = Foo('李杰')
obj2 = Foo('女神')

print(obj1.name)
print(obj2.name)

print(Foo.city)

print(obj1.city)
print(obj2.city)