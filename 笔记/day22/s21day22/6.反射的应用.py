#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server

class View(object):
    def login(self):
        return '登陆'

    def logout(self):
        return '等处'

    def index(self):
        return '首页'


def func(environ,start_response):
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    #
    obj = View()
    # 获取用户输入的URL
    method_name = environ.get('PATH_INFO').strip('/')
    if not hasattr(obj,method_name):
        return ["sdf".encode("utf-8"),]
    response = getattr(obj,method_name)()
    return [response.encode("utf-8")  ]

# 作用：写一个网站，用户只要来方法，就自动找到第三个参数并执行。
server = make_server('192.168.12.87', 8000, func)
server.serve_forever()

