#!/usr/bin/env python
# -*- coding:utf-8 -*-



# #################################
"""
def f1():
    print(123)
    return 666

result = f1()
print(result)
"""
# ###########################
# def func(arg):
#     def inner():
#         return arg()
#     return inner
#
# def f1():
#     print(123)
#     return 666
#
# v1 = func(f1)
# result = v1()
# print(result)




def func(arg):
    def inner():
        print('before')
        v = arg()
        print('after')
        return v
    return inner

# 第一步：执行func函数并将下面的函数参数传递，相当于：func(index)
# 第二步：将func的返回值重新赋值给下面的函数名。 index = func(index)
@func
def index():
    print(123)
    return 666






