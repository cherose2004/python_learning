#!/usr/bin/env python
# -*- coding:utf-8 -*-
class A:
    pass
    # def func(self):
    #     print('a')
class B(A):
    pass
    # def func(self):
    #     print('b')
class C(A):
    def func(self):
        print('c')
class D(B,C):
    pass
    # def func(self):
    #     print('d')
d = D()
d.func()
print(D.mro())
# DBCA
# DBAC