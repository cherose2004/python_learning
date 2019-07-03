#!/usr/bin/env python
# -*- coding:utf-8 -*-
info = []

def func(i):
    def inner():
        print(i)
    return inner

for item in range(10):
    info.append(func(item))

info[0]()
info[1]()
info[4]()
