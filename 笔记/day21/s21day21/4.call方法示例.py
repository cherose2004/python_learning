#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server

def func(environ,start_response):
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return ['你好'.encode("utf-8")  ]

class Foo(object):

    def __call__(self, environ,start_response):
        start_response("200 OK", [('Content-Type', 'text/html; charset=utf-8')])
        return ['你<h1 style="color:red;">不好</h1>'.encode("utf-8")]


# 作用：写一个网站，用户只要来方法，就自动找到第三个参数并执行。
server = make_server('192.168.12.87', 8000, Foo())
server.serve_forever()



