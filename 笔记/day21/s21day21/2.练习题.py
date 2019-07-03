#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""
"""
class StarkConfig(object):
    pass

class AdminSite(object):
    def __init__(self):
        self.data_list = []

    def register(self,arg):
        self.data_list.append(arg)

site = AdminSite()

obj = StarkConfig()
site.register(obj)
"""

"""
class StarkConfig(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

class AdminSite(object):
    def __init__(self):
        self.data_list = []
        self.sk = None

    def set_sk(self,arg):
        self.sk = arg


site = AdminSite() # data_list = []  sk = StarkConfig
site.set_sk(StarkConfig)
site.sk('alex',19)
"""

"""
class StackConfig(object):
    pass

class Foo(object):
    pass

class Base(object):
    pass

class AdminSite(object):
    def __init__(self):
        self._register = {}

    def registry(self,key,arg):
        self._register[key] = arg

site = AdminSite()
site.registry(1,StackConfig)
site.registry(2,StackConfig)
site.registry(3,StackConfig)
site.registry(4,Foo)
site.registry(5,Base)

for k,v in site._register.items():
    print(k,v() )
"""


class StackConfig(object):
    list_display = '李邵奇'

    def changelist_view(self):
        print(self.list_display)

class UserConfig(StackConfig):
    list_display = '利奇航'

class AdminSite(object):
    def __init__(self):
        self._register = {}

    def registry(self,key,arg=StackConfig):
        self._register[key] = arg

    def run(self):
        for key,value in self._register.items():
            obj = value()
            obj.changelist_view()
site = AdminSite()
site.registry(1)
site.registry(2,StackConfig)
site.registry(3,UserConfig)
site.run()



















