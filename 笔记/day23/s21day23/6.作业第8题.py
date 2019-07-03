#!/usr/bin/env python
# -*- coding:utf-8 -*-
MIDDLEWARE_CLASSES = [
    'utils.session.SessionMiddleware',
    'utils.auth.AuthMiddleware',
    'utils.csrf.CsrfMiddleware',
    'utils.element.ElementMiddleware',
]

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
    obj = View()
    method_name = environ.get('PATH_INFO').strip('/')
    if not hasattr(obj,method_name):
        return ["".encode("utf-8"),]
    response = getattr(obj,method_name)()
    # 对字符串的前后进行包装
    # msg = "【auth】【session】 %s 【session】 【auth】 " %response

    import importlib
    for path in MIDDLEWARE_CLASSES:
        module_path,cls_name = path.rsplit('.',maxsplit=1) # 'utils.session.SessionMiddleware',
        module = importlib.import_module(module_path) # from utils import session
        cls = getattr(module,cls_name)
        obj = cls()
        response = obj.process(response)


    return [response.encode("utf-8")  ]


server = make_server('127.0.0.1', 8000, func)
server.serve_forever()
