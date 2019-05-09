#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import struct
from socketserver import *
server_dir = r'D:\code\s21day30\文件传输优化\server_dir'

class Myserver(BaseRequestHandler):
    def my_recv(self,encoding='utf-8'):
        '''
        按照协议接收字典
        :param encoding:编码
        :return:从网络上接受到的字典格式的结果
        '''
        dic_len = self.request.recv(4)
        dic_len = struct.unpack('i', dic_len)[0]
        dic = self.request.recv(dic_len).decode(encoding)
        dic = json.loads(dic)
        return dic

    def my_send(self,dic,encoding='utf-8'):
        '''
        按照协议发送字典
        :param dic:要发送的字典内容
        :param encoding:编码
        :return:None
        '''
        str_dic = json.dumps(dic)  # 先把字典转换成str
        bdic = str_dic.encode(encoding)  # str转bytes
        dic_len = len(bdic)  # 计算bytes长度
        bytes_len = struct.pack('i', dic_len)
        self.request.send(bytes_len)  # 发送长度
        self.request.send(bdic)  # 发送字典

    def send_file(self,dic,filepath):
        '''
        发送文件
        :param dic:文件信息的字典
        :param filepath:待发送文件所在路径
        :return:None
        '''
        with open(filepath, 'rb') as f:
            while dic['filesize'] > 2048:
                content = f.read(2048)
                self.request.send(content)
                dic['filesize'] -= len(content)
            else:
                content = f.read()
                self.request.send(content)

    def download(self,dic):
        '''
        下载功能
        :param dic:客户端发来的字典信息，包含要下载的文件名
        :return:None
        '''
        filename = dic['filename']   # 获取文件名
        filepath = os.path.join(server_dir, filename)  # 拼接文件绝对路径
        dic = {}
        if os.path.isfile(filepath):   # 判断用户要下载的是否是个文件
            dic['filesize'] = os.path.getsize(filepath) # 获取文件大小
            dic['isfile'] = True       # 将信号设置为True，以便客户端判断文件是否可以执行下载逻辑
            self.my_send(dic)          # 发送字典信息
            self.send_file(dic, filepath)  # 发送文件
        else:
            dic['isfile'] = False      #  将信号设置为False，以便客户端判断文件是否可以执行下载逻辑
            self.my_send(dic)          #  发送字典信息
    def handle(self):
        dic = self.my_recv()
        if dic['operate'] == 'download':
            self.download(dic)



server = ThreadingTCPServer(('127.0.0.1',9000),Myserver)
server.serve_forever()