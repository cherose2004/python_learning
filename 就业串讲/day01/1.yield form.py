# -*- coding: utf-8 -*-
# __author__ = "maple"

def show():
    yield 88
    yield 99

def func():
    yield 1
    yield from show()
    yield 2

obj = func()
for item in obj:
    print(item)

