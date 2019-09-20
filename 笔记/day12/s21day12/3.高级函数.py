#!/usr/bin/env python
# -*- coding:utf-8 -*-

# v1 = [11,22,33,44]
# for i in range(0,len(v1)):
#     v1[i] = v1[i] + 100
# print(v1)

# v1 = [11,22,33,44]

# 第一个参数：必须是一个函数
# 第二个参数：必须可迭代类型（可以被for循环）
# def func(arg):
#     return arg + 100
# result = map(func,v1)# 然后将函数的返回值添加到 [None,None]
# print(list(result))
# result = map(lambda x:x+100,v1)
# print(result) # [111,122,133,144] # py2
# print(list(result)) # 特殊

import functools

# v1 = [1,2,3,4,5,6]
#
# def func(x,y):
#     return x*y
# result = functools.reduce(func,v1)
# print(result)

import functools
v1 = ['wo','hao','e']

result = functools.reduce(lambda x,y:x+y,v1)
print(result)