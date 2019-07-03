#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""

"""
def wrapper(func):
    print('wrapper函数')
    def inner(*args, **kwargs):
        print('inner')
        data = func(*args, **kwargs)  # 执行原函数并获取返回值
        return data
    return inner

@wrapper
def index():
    pass
"""


def x(counter):
    print('x函数')
    def wrapper(func):
        print('wrapper函数')
        def inner(*args,**kwargs):
            if counter:
                return 123
            return func(*args,**kwargs)
        return inner
    return wrapper

@x(True)
def fun990():
    pass

@x(False)
def func10():
    pass





