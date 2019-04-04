#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ######################## 读取:r,只读不能写 + 文件不存在报错 ##########################
"""
# 打开文件
file_object = open('log.txt',mode='r',encoding='utf-8') # r,read; w,write; a,append；

# 读取内容
content = file_object.read()
print(content)

# 关闭文件
file_object.close()
"""

# ######################## 写入：w，只写不能读（先清空文件） + 文件不存在则新建 ##########################
"""
# 打开文件
file_object = open('losssg.txt',mode='w',encoding='utf-8') # r,read(只读); w,write(只写,先清空，一般用于新建文件); a,append；

# 写内容
# file_object.write('鬼厉')

# 关闭文件
file_object.close()
"""

# ######################## 写入：a，只追加不能读 + 不存在则新建 ##########################
"""
# 打开文件
file_object = open('logfffff.txt',mode='a',encoding='utf-8') # r,read(只读); w,write(只写,先清空，一般用于新建文件); a,append；
# 写内容
file_object.write('你好')

# 关闭文件
file_object.close()
"""
