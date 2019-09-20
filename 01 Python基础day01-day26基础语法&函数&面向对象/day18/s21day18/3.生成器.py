#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# def func():
#     result = []
#     for i in range(10):
#         result.append(i)
#     return result
# v1 = func()
v1 = [i for i in range(10)] # 列表推导式，立即循环创建所有元素。
print(v1)

# def func():
#     for i in range(10):
#         yield i
# v2 = func()
v2 = (i for i in range(10)) # 生成器推导式，创建了一个生成器，内部循环为执行。
"""

"""
def func():
    result = []
    for i in range(10):
        def f():
            return i
        result.append(f)
    return result

v1 = func()
for item in v1:
    print(item())
    
# v1 = [lambda :i for i in range(10)]
# for item in v1:
#     print(item())
"""



# def func():
#     for i in range(10):
#         def f():
#             return i
#         yield f
#
# v1 = func()
# for item in v1:
#     print(item())
v1 = (lambda :i for i in range(10))
for item in v1:
    print(item())






