#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
from multiprocessing import Process
def chat(conn):
    while True:
        try:
            ret = conn.recv(1024).decode('utf-8')
            conn.send(ret.upper().encode('utf-8'))
        except ConnectionResetError:
            break

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9000))
    sk.listen()
    while True:
        conn,_ = sk.accept()
        Process(target=chat,args=(conn,)).start()












