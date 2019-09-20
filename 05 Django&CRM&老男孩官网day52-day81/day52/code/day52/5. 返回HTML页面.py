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


def index(url):
    with open('index.html','rb') as f:
        ret = f.read()
    return ret


def home(url):
    ret = '<h1>home!</h1>({})'.format(url)
    return ret.encode('utf-8')


list1 = [
    ('/index', index),
    ('/home', home),
]

while True:
    conn, addr = sk.accept()
    # 接收数据
    data = conn.recv(1024)
    data = data.decode('utf-8')
    url = data.split()[1]
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    func = None
    for i in list1:
        if url == i[0]:
            func = i[1]
            break
    if func:
        ret = func(url)
    else:
        ret = b'<h1>404 not found!</h1>'
    conn.send(ret)
    # 断开连接
    conn.close()
