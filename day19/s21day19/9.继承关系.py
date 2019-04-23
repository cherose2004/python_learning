#!/usr/bin/env python
# -*- coding:utf-8 -*-
from socketserver import ThreadingTCPServer



t = ThreadingTCPServer()
t.serve_forever()