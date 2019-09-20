#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import struct
from socketserver import *
server_dir = r'D:\code\s21day30\文件传输\server_dir'

class Myserver(BaseRequestHandler):
    def handle(self):
        dic_len = self.request.recv(4)
        dic_len = struct.unpack('i',dic_len)[0]
        dic =self.request.recv(dic_len).decode('utf-8')
        dic = json.loads(dic)
        if dic['operate'] == 'download':
            filename = dic['filename']
            filepath = os.path.join(server_dir,filename)
            dic = {}
            if os.path.isfile(filepath):
                dic['filesize'] = os.path.getsize(filepath)
                dic['isfile'] = True
            else:
                dic['isfile'] = False
            str_dic = json.dumps(dic)  #先把字典转换成str
            bdic = str_dic.encode('utf-8')   # str转bytes
            dic_len = len(bdic)   # 计算bytes长度
            bytes_len = struct.pack('i',dic_len)
            self.request.send(bytes_len)  # 发送长度
            self.request.send(bdic)       # 发送字典

            if dic['isfile']:
                with open(filepath,'rb') as f:
                    while dic['filesize'] > 2048:
                        content = f.read(2048)
                        self.request.send(content)
                        dic['filesize'] -= len(content)
                    else:
                        content = f.read()
                        self.request.send(content)

server = ThreadingTCPServer(('127.0.0.1',9000),Myserver)
server.serve_forever()