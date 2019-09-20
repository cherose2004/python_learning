#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

file_path = input('>>>')
if os.path.isabs(file_path):
    filename = os.path.basename(file_path)
    filesize = os.path.getsize(file_path)
    dic = {'filename':filename,'filesize':filesize}
    str_dic = json.dumps(dic)
    sk.send(str_dic.encode('utf-8'))
    with open(file_path,mode = 'rb') as f:
        content = f.read()
        sk.send(content)
sk.close()