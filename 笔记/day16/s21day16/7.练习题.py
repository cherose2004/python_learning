#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import shutil
from datetime import datetime
ctime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# 1.压缩lizhongwei文件夹 zip
# 2.放到到 code 目录（默认不存在）
# 3.将文件解压到D:\x1目录中。

if not os.path.exists('code'):
    os.makedirs('code')
shutil.make_archive(os.path.join('code',ctime),'zip','D:\code\s21day16\lizhongwei')

file_path = os.path.join('code',ctime) + '.zip'
shutil.unpack_archive(file_path,r'D:\x1','zip')