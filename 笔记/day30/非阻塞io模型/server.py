#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 阻塞io模型
# 非阻塞io模型
# 事件驱动io
# io多路复用
# 异步io模型

import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.setblocking(False)
sk.listen()

conn_l = []
del_l = []
while True:
    try:
        conn,addr = sk.accept()   # 阻塞，直到有一个客户端来连我
        print(conn)
        conn_l.append(conn)
    except BlockingIOError:
        for c in conn_l:
            try:
                msg = c.recv(1024).decode('utf-8')
                if not msg:
                    del_l.append(c)
                    continue
                print('-->',[msg])
                c.send(msg.upper().encode('utf-8'))
            except BlockingIOError:pass
        for c in del_l:
            conn_l.remove(c)
        del_l.clear()
sk.close()

# socket的非阻塞io模型 + io多路复用实现的
    # 虽然非阻塞，提高了CPU的利用率，但是耗费CPU做了很多无用功