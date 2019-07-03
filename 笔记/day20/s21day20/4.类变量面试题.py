#!/usr/bin/env python
# -*- coding:utf-8 -*-
# class Base:
#     x = 1
#
# obj = Base()
#
#
# print(obj.x) # 先去对象中找，没有再去类中找。
# obj.y = 123  # 在对象中添加了一个y=123的变量。
# print(obj.y)
# obj.x = 123
# print(obj.x)
# print(Base.x)


"""
class Base:
    x = 1

class Foo(Base):
    pass

print(Base.x)
print(Foo.x)
Base.x = 666
print(Base.x)
print(Foo.x)
Foo.x = 999
print(Base.x)
print(Foo.x)
"""

"""
class Parent:
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x,Child1.x,Child2.x) # 1 1 1
Child1.x = 2
print(Parent.x,Child1.x,Child2.x) # 1 2 1
Child2.x = 3
print(Parent.x,Child1.x,Child2.x) # 1 2 3

"""


class Parent:
    x = 1

class Child(Parent):
    pass

obj = Child()
print(obj.x)
obj.x = 2
print(Child.x)


