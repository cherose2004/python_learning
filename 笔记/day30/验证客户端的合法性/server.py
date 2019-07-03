#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import hashlib
import socket

def get_md5(secret_key,randseq):
    md5 = hashlib.md5(secret_key)
    md5.update(randseq)
    res = md5.hexdigest()
    return res

def chat(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
        conn.send(msg.upper().encode('utf-8'))

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

secret_key = b'alexsb'
while True:
    conn,addr = sk.accept()
    randseq = os.urandom(32)
    conn.send(randseq)
    md5code = get_md5(secret_key,randseq)
    ret = conn.recv(32).decode('utf-8')
    print(ret)
    if ret == md5code:
        print('是合法的客户端')
        chat(conn)
    else:
        print('不是合法的客户端')
        conn.close()
sk.close()