#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import socket
import time

def get_md5(secret_key,randseq):
    md5 = hashlib.md5(secret_key)
    md5.update(randseq)
    res = md5.hexdigest()
    return res
def chat(sk):
    while True:
        sk.send(b'hello')
        msg = sk.recv(1024).decode('utf-8')
        print(msg)
        time.sleep(0.5)
sk = socket.socket()
sk.connect(('127.0.0.1',9000))

secret_key = b'alexsb'
randseq = sk.recv(32)
md5code = get_md5(secret_key,randseq)

sk.send(md5code.encode('utf-8'))
chat(sk)

sk.close()