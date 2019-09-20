#!/usr/bin/env python
# -*- coding:utf-8 -*-

v = [11, 2, 33, 4]

def func(arg):
    print('内',id(arg))

print('外',id(v))  # 列表内存地址
func(v)