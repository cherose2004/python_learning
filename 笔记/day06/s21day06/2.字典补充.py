#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 索引不存在，报错
# v = ['alex','oldboy']
# print(v[123])

# ################ get
"""
info = {'k1':'v1','k2':'v2'}

# v1 = info['k11111']
# v2 = info.get('k1111') # None就是Python中的空
# v3 = info.get('k1111',666)
# print(v2)

result = info.get('k1111')
if result == None:
    print('不存在')

if result:
    print('存在')
else:
    print('不存再')
"""

# ################ get
# info = {'k1':'v1','k2':'v2'}
# result = info.pop('k2')
# print(info,result)
#
# del info['k1']

# ################ update
info = {'k1':'v1','k2':'v2'}

# 不存在，则添加/存在，则更新
info.update({'k3':'v3','k4':'v4','k2':666})
print(info)