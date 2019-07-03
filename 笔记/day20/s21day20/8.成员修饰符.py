#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Base:
    def __f1(self):
        print('Base.f1')
class Foo(Base):

    def fun(self):
        self.__f1()


obj = Foo()
obj.fun()
