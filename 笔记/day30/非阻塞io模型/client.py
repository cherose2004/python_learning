#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
for i in range(30):
    sk.send(b'wusir')
    msg = sk.recv(1024)
    print(msg)
    time.sleep(0.2)
sk.close()