# -*- coding: utf-8 -*-
# __author__ = "maple"

from socket import socket,SOCK_DGRAM
udpcli = socket(type=SOCK_DGRAM)
server = ('127.0.0.1',9002)

udpcli.sendto(b'msg',server)
msg = udpcli.recv(1024)
print(msg.decode())

udpcli.close()