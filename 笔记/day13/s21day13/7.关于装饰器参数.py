#!/usr/bin/env python
# -*- coding:utf-8 -*-
def wrapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@wrapper
def index():
    print(1123)
index()

@wrapper
def show(a1):
    print(a1+100)

show(1)