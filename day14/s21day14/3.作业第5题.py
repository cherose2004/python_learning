#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

def wrapper(func):
    def inner(*args,**kwargs):
        value = []
        for i in range(5):
            data = func(*args,**kwargs)
            value.append(data)
        return value
    return inner

@wrapper
def func():
    return random.randint(1,4)

reuslt = func() # 执行5次，并将每次执行的结果追加到列表最终返回给result
print(reuslt)