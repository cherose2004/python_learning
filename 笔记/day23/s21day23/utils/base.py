#!/usr/bin/env python
# -*- coding:utf-8 -*-

class BaseMiddlware(object):
    def process(self,data):
        raise NotImplementedError('字类必须实现process方法')