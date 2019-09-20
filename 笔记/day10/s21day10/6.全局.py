#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = []
def func():
    # name.append(123)
    global name
    name = 123
func()

print(name)