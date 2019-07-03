#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.base import BaseMiddlware

class CsrfMiddleware(BaseMiddlware):
    def process(self,data):
        msg = "【csrf】%s【csrf】" % data
        return msg