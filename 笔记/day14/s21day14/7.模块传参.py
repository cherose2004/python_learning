#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
让用户执行脚本传入要删除的文件路径，在内部帮助用将目录删除。
C:\Python36\python36.exe D:/code/s21day14/7.模块传参.py D:/test
C:\Python36\python36.exe D:/code/s21day14/7.模块传参.py

"""
import sys

# 获取用户执行脚本时，传入的参数。
# C:\Python36\python36.exe D:/code/s21day14/7.模块传参.py D:/test
# sys.argv = [D:/code/s21day14/7.模块传参.py, D:/test]
path = sys.argv[1]

# 删除目录
import shutil
shutil.rmtree(path)
