#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9000))

msg = sk.recv(1024)
print(msg)
sk.send(b'byebye')

sk.close()