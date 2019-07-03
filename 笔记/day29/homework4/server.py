#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import socket

sk = socket.socket()
sk.bind(('192.168.12.87',9000))
sk.listen()

conn,addr = sk.accept()
print(addr)
str_dic = conn.recv(1024).decode('utf-8')
dic = json.loads(str_dic)
content = conn.recv(dic['filesize'])
with open(dic['filename'],mode='wb') as f:
    f.write(content)
conn.close()
sk.close()











