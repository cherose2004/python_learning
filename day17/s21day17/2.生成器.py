#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""
"""
def func():
    count = 1
    while True:
        yield count
        count += 1

val = func()
for item in val:
    print(item)
"""

def func():
    count = 1
    while True:
        yield count
        count += 1
        if count == 100:
            return

val = func()
for item in val:
    print(item)
