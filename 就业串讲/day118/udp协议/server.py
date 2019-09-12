# -*- coding: utf-8 -*-
# __author__ = "maple"

from socket import socket,SOCK_DGRAM
udpserver = socket(type=SOCK_DGRAM)
udpserver.bind(('127.0.0.1',9002))

msg,cli_addr = udpserver.recvfrom(1024)
print(msg.decode())
udpserver.sendto(b'message',cli_addr)

udpserver.close()

