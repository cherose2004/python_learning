#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MyException(Exception):
    def __init__(self,message):
        super().__init__()
        self.message = message

try:
    raise MyException('asdf')
except MyException as e:
    print(e.message)
