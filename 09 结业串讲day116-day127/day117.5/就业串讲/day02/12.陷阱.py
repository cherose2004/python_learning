# -*- coding: utf-8 -*-
# __author__ = "maple"


def func(a,b=[]):
    return b.append(a)

# 方式一
# v1 = func(11)
# v2 = func(22,[])
# v3 = func(33)
# print(v1,v2,v3)
# 方式二
# v1 = func(11)
# print(v1)
# v2 = func(22,[])
# print(v2)
# v3 = func(33)
# print(v3)