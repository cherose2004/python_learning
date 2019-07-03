#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000))
while True:
    msg,client_addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    msg = input('>>>').encode('utf-8')
    sk.sendto(msg,client_addr)
sk.close()
# udp协议
# 基础需求：
    # 能随时退出
    # 能实现一个人和多个人聊天
    # 并且给每个人标识一个身份
    # 每个身份一种颜色
# 进阶需求：
    # 多个人能同时互相聊
