#!/usr/bin/env python
# -*- coding:utf-8 -*-


def func(max_range):
    result = [1,1]
    while True:

        val = result[-1] + result[-2]
        if val > max_range:
            break
        result.append(val)
    return result

v = func(100)
print(v)