#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import os
# path = "D:\code\s21day14" # user/index/inx/fasd/
# v = 'n.txt'
#
# result = os.path.join(path,v)
# print(result)
# result = os.path.join(path,'n1','n2','n3')
# print(result)

import os

result = os.walk(r'D:\code\s21day14')
for a,b,c in result:
    # a,正在查看的目录 b,此目录下的文件夹  c,此目录下的文件
    for item in c:
        path = os.path.join(a,item)
        print(path)

