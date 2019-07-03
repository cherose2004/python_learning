#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from datetime import datetime,timezone,timedelta

# ######################## 获取datetime格式时间 ##############################
"""
v1 = datetime.now() # 当前本地时间
print(v1)
tz = timezone(timedelta(hours=7)) # 当前东7区时间
v2 = datetime.now(tz)
print(v2)
v3 = datetime.utcnow() # 当前UTC时间
print(v3)
"""

# ######################## 把datetime格式转换成字符串 ##############################
# v1 = datetime.now()
# print(v1,type(v1))
# val = v1.strftime("%Y-%m-%d %H:%M:%S")
# print(val)

# ######################## 字符串转成datetime ##############################
# v1 = datetime.strptime('2011-11-11','%Y-%m-%d')
# print(v1,type(v1))

# ######################## datetime时间的加减 ##############################
# v1 = datetime.strptime('2011-11-11','%Y-%m-%d')
# v2 = v1 - timedelta(days=140)
# date = v2.strftime('%Y-%m-%d')
# print(date)

# ######################## 时间戳和datetime关系 ##############################
# ctime = time.time()
# print(ctime)
# v1 = datetime.fromtimestamp(ctime)
# print(v1)

# v1 = datetime.now()
# val = v1.timestamp()
# print(val)

