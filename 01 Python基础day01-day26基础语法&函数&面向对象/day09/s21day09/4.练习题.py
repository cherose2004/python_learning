#!/usr/bin/env python
# -*- coding:utf-8 -*-
def num(l):
    count = 0
    for i in l:
        if type(i) == int:
            count += 1
    return count
li = ['salkdj',6,66,677,'skajhd','ksjad']
a = num(li)
print('列表中有%d个数字'%(a,))