#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ###################################### 读操作
# file_object = open('log.txt',mode='r',encoding='utf-8')

# 读取文件的所有内容到内存
# data = file_object.read()

# 从当前光标所在的位置向后读取文件两个字符
# data = file_object.read(2)

# 读取文件的所有内容到内存，并按照每一行进行分割到列表中。
# data_list = file_object.readlines()
# print(data_list)

# 如果以后读取一个特别大的文件 (**********)
# for line in file_object:
#     line = line.strip()
#     print(line)

# file_object.close()
# ###################################### 写操作
"""
file_object = open('log.txt',mode='w',encoding='utf-8')
file_object.write('asdfadsfasdf\n')
file_object.write('asdfasdfasdfsadf')
file_object.close()
"""