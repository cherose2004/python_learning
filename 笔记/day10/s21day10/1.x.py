#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open('x',mode='r',encoding='utf-8')
v = []
for line in f:
    line = line.strip() # 'alex,123'
    row_list = line.split(',') # ['alex','123']
    # v.extend(row_list)
    for item in row_list:
        v.append(item)

print(v)