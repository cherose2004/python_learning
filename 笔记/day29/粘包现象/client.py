#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

sk.send(b'hello')
sk.send(b'world')

sk.close()