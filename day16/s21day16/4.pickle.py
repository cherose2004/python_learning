#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle

# #################### dumps/loads ######################
"""
v = {1,2,3,4}
val = pickle.dumps(v)
print(val)
data = pickle.loads(val)
print(data,type(data))
"""

"""
def f1():
    print('f1')

v1 = pickle.dumps(f1)
print(v1)
v2 = pickle.loads(v1)
v2()
"""

# #################### dump/load ######################
# v = {1,2,3,4}
# f = open('x.txt',mode='wb')
# val = pickle.dump(v,f)
# f.close()

# f = open('x.txt',mode='rb')
# data = pickle.load(f)
# f.close()
# print(data)