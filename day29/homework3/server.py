#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import socket
import hashlib
def get_md5(username,password):
    md5 = hashlib.md5(username.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,_ = sk.accept()
str_dic = conn.recv(1024).decode('utf-8')
dic = json.loads(str_dic)
with open('userinfo',encoding='utf-8') as f:
    for line in f:
        user,passwd = line.strip().split('|')
        if user == dic['usr'] and passwd == get_md5(dic['usr'],dic['pwd']):
            res_dic = {'opt':'login','result':True}
            break
    else:
        res_dic = {'opt': 'login', 'result': False}
sdic = json.dumps(res_dic)
conn.send(sdic.encode('utf-8'))
conn.close()
sk.close()





















