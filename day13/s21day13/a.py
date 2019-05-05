#!/usr/bin/env python
# -*- coding:utf-8 -*-

def wrapper(func):
    def inner():
        print('登陆')
        v = func()
        return v
    return inner

@wrapper
def f1():
    print(1)

@wrapper
def f2():
    print(2)

@wrapper
def f3():
    print(3)