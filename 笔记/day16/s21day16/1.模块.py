#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# 导入模块，加载此模块中所有的值到内存。
import lizhongwei
print(123)
# 调用模块中的函数
lizhongwei.func()
"""

from lizhongwei import func as f

def func():
    print(123)
f()