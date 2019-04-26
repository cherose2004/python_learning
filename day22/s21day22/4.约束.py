#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Interface(object):
    def send(self):
        raise NotImplementedError()

class Message(Interface):
    def send(self):
        print('发送短信')

class Email(Interface):
    pass