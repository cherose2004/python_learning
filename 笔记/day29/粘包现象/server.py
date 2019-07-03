#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import struct
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,_ = sk.accept()
byte_len = conn.recv(4)
size = struct.unpack('i',byte_len)[0]
msg1 = conn.recv(size)
print(msg1)
byte_len = conn.recv(4)
size = struct.unpack('i',byte_len)[0]
msg2 = conn.recv(size)
print(msg2)
conn.close()
sk.close()

# 发送4个字节的文件的信息
# json --》文件的大小+文件名。。。。
# 发送文件

