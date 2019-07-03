#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Foo:
    def __init__(self):
        self.name = 123

    def func(self, a, b):
        print(self.name, a, b)

    @staticmethod
    def f1():
        print(123)

    @classmethod
    def f2(cls,a,b):
        print('cls是当前类',cls)
        print(a,b)

obj = Foo()
obj.func(1, 2)

Foo.f1()
Foo.f2(1,2)
