#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import socket
def client(i):
    sk = socket.socket()
    sk.connect(('127.0.0.1',9000))

    while True:
        sk.send('hello'.encode('utf-8'))
        print(i*'*',sk.recv(1024))
        time.sleep(0.5)

from threading import Thread
for i in range(500):
    Thread(target=client,args =(i,)).start()