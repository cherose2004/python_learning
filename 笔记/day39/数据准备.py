#!/usr/bin/env python
# -*- coding:utf-8 -*-
from uuid import uuid1
with open('file','w') as f:
    for i in range(2700000):
        f.write(str(uuid1(i))+'\n')