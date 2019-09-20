#!/usr/bin/env python
# -*- coding:utf-8 -*-
import gevent
from gevent import monkey
monkey.patch_all()
import socket

def chat(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        conn.send(msg.upper().encode('utf-8'))

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

while True:
    conn,_ = sk.accept()
    gevent.spawn(chat,conn)

# 5*20*500 = 50000
