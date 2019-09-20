#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()    # n 允许多少客户端等待
print('*'*20)
while True:   # outer
    conn,addr = sk.accept()    # 阻塞
    print(addr)
    while True:   # inner
        msg = conn.recv(1024).decode('utf-8')
        if msg.upper() == 'Q': break
        print(msg)
        inp = input('>>>')
        conn.send(inp.encode('utf-8'))
        if inp.upper() == 'Q':
            break
    conn.close()
sk.close()

# 想说啥说啥   input
# 想说多久说多久   while True:   # inner
# 和一个人聊完再和另一个人聊   while True:   # outer


