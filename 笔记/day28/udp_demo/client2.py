#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    inp = input('>>>').encode('utf-8')
    sk.sendto(inp,('127.0.0.1',9000))
    ret = sk.recv(1024)
    print(ret)
sk.close()