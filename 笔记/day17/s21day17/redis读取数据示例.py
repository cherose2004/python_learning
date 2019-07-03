#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

conn = redis.Redis(host='192.168.11.11')

# scan_iter,是一个生成器函数
result = conn.scan_iter(count=100)
for item in result:
    print(item)



conn.close()