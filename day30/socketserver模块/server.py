#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):  # 自动触发了handle方法，并且self.request == conn
        msg = self.request.recv(1024).decode('utf-8')
        self.request.send('1'.encode('utf-8'))
        msg = self.request.recv(1024).decode('utf-8')
        self.request.send('2'.encode('utf-8'))
        msg = self.request.recv(1024).decode('utf-8')
        self.request.send('3'.encode('utf-8'))

server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
server.serve_forever()