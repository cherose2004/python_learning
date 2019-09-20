# -*- coding: utf-8 -*-
# __author__ = "maple"

from socket import socket

tcp_client = socket()


tcp_client.connect(('127.0.0.1',9001))
msg = tcp_client.recv(1024)
print(msg)
tcp_client.send(b'message')

tcp_client.close()
