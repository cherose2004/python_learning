#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import hmac
import socket

def get_md5(secret_key,randseq):
    h = hmac.new(secret_key,randseq)
    res = h.digest()
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
    hmaccode = get_md5(secret_key,randseq)
    ret = conn.recv(16)
    print(ret)
    if ret == hmaccode:
        print('是合法的客户端')
        chat(conn)
    else:
        print('不是合法的客户端')
        conn.close()
sk.close()