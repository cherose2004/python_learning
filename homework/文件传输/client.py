#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import struct
import socket
local_dir = r'D:\code\s21day30\文件传输\local_dir'
sk = socket.socket()
sk.connect(('127.0.0.1',9000))

# 下载
    # 从哪个路径下载
    # 下载之后放哪儿
        # 都放到固定目录
        # 指定目录放

filename = input('>>>').strip()
dic = {'filename':filename,'operate':'download'}
str_dic = json.dumps(dic)  #先把字典转换成str
bdic = str_dic.encode('utf-8')   # str转bytes
dic_len = len(bdic)   # 计算bytes长度
bytes_len = struct.pack('i',dic_len)
sk.send(bytes_len)  # 发送长度
sk.send(bdic)       # 发送字典

dic_len = sk.recv(4)  # 接受要下载的文件信息
dic_len = struct.unpack('i',dic_len)[0]
dic = sk.recv(dic_len).decode('utf-8')
dic = json.loads(dic)

if dic['isfile']:
    filepath = os.path.join(local_dir,filename)
    with open(filepath,'wb') as f:
        while dic['filesize'] > 2048:
            content = sk.recv(2048)
            f.write(content)
            dic['filesize'] -= len(content)

        else:
            while dic['filesize']:
                content = sk.recv(dic['filesize'])
                f.write(content)
                dic['filesize'] -= len(content)
else:
    print('您要下载的文件不存在')

