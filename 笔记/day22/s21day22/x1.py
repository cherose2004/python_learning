#!/usr/bin/env python
# -*- coding:utf-8 -*-

NUM = 1999
def func():
    print('func')

class Foo(object):
    X = 1
    def show(self):
        print('Foo.show')
    @staticmethod
    def info():
        print('info')