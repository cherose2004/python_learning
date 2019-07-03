#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

# 1. 读取文件大小（字节）
file_size = os.stat('20190409_192149.mp4').st_size

# 2.一点一点的读取文件
read_size = 0
with open('20190409_192149.mp4',mode='rb') as f1,open('a.mp4',mode='wb') as f2:
    while read_size < file_size:
        chunk = f1.read(1024) # 每次最多去读取1024字节
        f2.write(chunk)
        read_size += len(chunk)
        val = int(read_size / file_size * 100)
        print('%s%%\r' %val ,end='')