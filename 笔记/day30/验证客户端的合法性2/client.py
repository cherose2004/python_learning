#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import time
import hmac

def get_md5(secret_key,randseq):
    h = hmac.new(secret_key,randseq)
    res = h.digest()
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
hmaccode = get_md5(secret_key,randseq)

sk.send(hmaccode)
chat(sk)

sk.close()