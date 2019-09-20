# -*- coding: utf-8 -*-
# __author__ = "maple"

from socketserver import BaseRequestHandler,ThreadingTCPServer

class Myserver(BaseRequestHandler):
    def handle(self):
        # conn = self.request
        self.request.send(b'hello')
        msg = self.request.recv(1024)
        print(msg)
server = ThreadingTCPServer(('0.0.0.0',9001),Myserver)
server.serve_forever()

