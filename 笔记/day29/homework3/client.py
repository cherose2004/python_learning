#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import socket

usr = input('username : ')
pwd = input('password : ')
dic = {'usr':usr,'pwd':pwd}
str_dic = json.dumps(dic)
sk = socket.socket()
sk.connect(('127.0.0.1',9000))

sk.send(str_dic.encode('utf-8'))
ret = sk.recv(1024).decode('utf-8')
ret_dic = json.loads(ret)
if ret_dic['result']:
    print('登陆成功')
sk.close()













