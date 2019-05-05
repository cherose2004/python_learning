#!/usr/bin/env python
# -*- coding:utf-8 -*-

def func():
    """
    分批去读取文件中的内容，将文件的内容返回给调用者。
    :return:
    """
    cursor = 0
    while True:
        f = open('db', 'r', encoding='utf-8')# 通过网络连接上redis
        # 代指   redis[0:10]
        f.seek(cursor)
        data_list =[]
        for i in range(10):
            line = f.readline()
            if not line:
                return
            data_list.append(line)
        cursor = f.tell()
        f.close()  # 关闭与redis的连接


        for row in data_list:
            yield row


for item in func():
    print(item)