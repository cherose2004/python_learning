#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import time
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
for i in range(3):
    sk.send(b'hello,wusir')
    msg = sk.recv(1024)
    print(msg)
    time.sleep(1)

sk.close()