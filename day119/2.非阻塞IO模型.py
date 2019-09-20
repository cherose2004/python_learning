# -*- coding: utf-8 -*-
# __author__ = "maple"

import socket

sk  = socket.socket()
sk.setblocking(False)  # 设置为非阻塞
sk.bind(('127.0.0.1',9000))
sk.listen()
conn_l = []
while True:
    try:
        conn,addr = sk.accept()
        conn_l.append(conn)
    except BlockingIOError:
        for conn in conn_l:
            try:
                msg = conn.recv(1024).decode('utf-8')
                if msg:
                    print(msg)
                conn.send(msg.upper().encode('utf-8'))
            except BlockingIOError:
                pass