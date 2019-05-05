#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

# 获取一个值的应用计数
"""
a = [11,22,33]
b = a
print(sys.getrefcount(a))
"""

# python默认支持的递归数量
"""
v1 = sys.getrecursionlimit()
"""


# 输入输出
# sys.stdout.write('你好')
# sys.stdout.write('呀')
# \n 换行
# \t 制表符
# \r ,回到当前行的起始位置
# print('1231你好你好你好23\r',end='')
# print('你好',end='')
"""
import time
for i in range(1,101):
    msg = "%s%%\r" %i
    print(msg,end='')
    time.sleep(0.05)
"""

# 1.

