#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""
# 可读可写
"""
读取
写入：根据光标的位置，从当前光标位置开始进行写入操作（可能会将其他的文字覆盖）
"""
"""
file_object = open('log.txt',mode='r+',encoding='utf-8')
# file_object.seek(2) # 调整光标的位置

content = file_object.read()
file_object.write('浪')

# # 读取内容
# content = file_object.read()
# print(content)
#
# file_object.write('666')

# 关闭文件
file_object.close()
"""

# 可读可写
# 写入时会将文件清空，读取时需要调整光标
"""
file_object = open('log.txt',mode='w+',encoding='utf-8')
data = file_object.read()
print(data)
file_object.write('alex')
file_object.seek(0)
data = file_object.read()
print(data)
file_object.close()
"""

# 可读可写
file_object = open('log.txt',mode='a+',encoding='utf-8')

# file_object.seek(0)
# data = file_object.read()
# print(data)

file_object.seek(0)
file_object.write('666')

file_object.close()