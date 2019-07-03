#!/usr/bin/env python
# -*- coding:utf-8 -*-
name = 'alex'
def func(v):
    def inner():
        print(name)
    return inner
v1 =func('alex')
v2 =func('eric')
