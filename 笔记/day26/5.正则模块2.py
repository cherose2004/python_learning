#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 进阶方法
# 1.时间复杂度  效率  compile
    # 在同一个正则表达式重复使用多次的时候使用能够减少时间的开销
# 2.空间复杂度  内存占用率   finditer
    # 在查询的结果超过1个的情况下，能够有效的节省内存，降低空间复杂度，从而也降低了时间复杂度
# 3.用户体验

import re

# ret = re.findall('\d','safhl02urhefy023908'*20000000)
# print(ret)

# ret = re.finditer('\d','safhl02urhefy023908'*20000000)  # ret是迭代器
# for i in ret:    # 迭代出来的每一项都是一个对象
#     print(i.group())  # 通过group取值即可

# compile
# s = '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>' \
#     '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>'
# ret = re.compile('\d3')
# print(ret)
# r1 = ret.search('alex83')
# print(r1)
# ret.findall('wusir74')
# ret = re.compile('\d+')
# r3 = ret.finditer('taibai40')
# for i in r3:
#     print(i.group())

# \d 正则表达式  ——> 字符串
    # \d  str
        # 循环str，找到所有的数字

# findall search
# finditer compile

# sub
# split
# import re
# ret = re.split('\d(\d)','alex83wusir74taibai')  # 默认自动保留分组中的内容
# print(ret)

# ret = re.sub('\d','D','alex83wusir74taibai',1)
# print(ret)

# ret = re.subn('\d','D','alex83wusir74taibai')
# print(ret)


# findall 参数顺序和数据类型，返回值类型
# search
# match

# finditer
# compile

# sub subn
# split