#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import struct
import socket

local_dir = r'D:\code\s21day30\文件传输优化\local_dir'
sk = socket.socket()
sk.connect(('127.0.0.1',9000))

def mysend(sk,dic,encoding = 'utf-8'):
    str_dic = json.dumps(dic)  # 先把字典转换成str
    bdic = str_dic.encode(encoding)  # str转bytes
    dic_len = len(bdic)  # 计算bytes长度
    bytes_len = struct.pack('i', dic_len)
    sk.send(bytes_len)  # 发送长度
    sk.send(bdic)  # 发送字典

def myrecv(encoding = 'utf-8'):
    dic_len = sk.recv(4)  # 接受要下载的文件信息
    dic_len = struct.unpack('i', dic_len)[0]
    dic = sk.recv(dic_len).decode(encoding)
    dic = json.loads(dic)
    return dic

def recv_file(filename,sk,dic,buffer = 2048):
    '''
    接收文件
    :param filename: 文件名
    :param sk: socket对象
    :param dic: 存的是文件的大小等信息
    :param buffer: 默认一次收取的数据长度
    :return:
    '''
    def inner_recv(buffersize = buffer,recvsize = buffer):
        '''
        按照buffersize进行判断，接收recvsize长度的内容，并写文件
        '''
        while dic['filesize'] > buffersize:
            content = sk.recv(recvsize)
            f.write(content)
            dic['filesize'] -= len(content)
    filepath = os.path.join(local_dir, filename)
    with open(filepath, 'wb') as f:   # 打开文件
        inner_recv()    # 接收数据，每次接收2048个，直到剩余内容小于等于2048
        inner_recv(0,dic['filesize']) # 接收剩余的2048个以内的字节，直到全部接收完

filename = input('>>>').strip()
dic = {'filename':filename,'operate':'download'}
mysend(sk,dic)   # 发送要下载字典的信息
dic = myrecv()   # 接收结果，内容包括是否能下载，以及要下载的文件大小等信息
if dic['isfile']:
    recv_file(filename,sk,dic)
else:
    print('您要下载的文件不存在')

