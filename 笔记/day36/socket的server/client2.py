#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

while True:
    sk.send('hello'.encode('utf-8'))
    print(sk.recv(1024))
    time.sleep(0.5)