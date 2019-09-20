#!/usr/bin/env python
# -*- coding:utf-8 -*-
class FileHelper(object):
    instance = None
    def __init__(self, path):
        self.file_object = open(path,mode='r',encoding='utf-8')

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance


obj1 = FileHelper('x')
obj2 = FileHelper('x')
