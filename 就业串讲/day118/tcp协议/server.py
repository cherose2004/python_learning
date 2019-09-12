# -*- coding: utf-8 -*-
# __author__ = "maple"

from socket import socket

tcp_server = socket()
tcp_server.bind(('127.0.0.1',9001))
tcp_server.listen()

request,_ = tcp_server.accept()
request.send(b'hello')
msg = request.recv(1024)
print(msg)
request.close()

tcp_server.close()


