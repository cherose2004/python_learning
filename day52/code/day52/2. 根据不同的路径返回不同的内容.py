#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

# 创建一个socket对象
sk = socket.socket()
# 绑定IP和端口
sk.bind(('127.0.0.1', 8000))
# 监听
sk.listen(5)
# 等待连接
while True:
    conn, addr = sk.accept()
    # 接收数据
    data = conn.recv(1024)
    data = data.decode('utf-8')
    url = data.split()[1]
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')

    if url == '/index':
        # 返回数据
        conn.send(b'<h1>index!</h1>')
    elif url == '/home':
        conn.send(b'<h1>home!</h1>')
    else:
        conn.send(b'<h1>404 not found!</h1>')

    # 断开连接
    conn.close()
