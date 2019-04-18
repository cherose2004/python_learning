#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

v = {'k1':'alex','k2':'李杰'}

f = open('x.txt',mode='r',encoding='utf-8')

data = json.load(f)
f.close()

print(data,type(data))