# -*- coding: utf-8 -*-
# __author__ = "maple"


class Foo(object):

    def __init__(self,name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 对象（内部没有数据）
        data = object.__new__(cls)
        return data

obj = Foo('李鹏')