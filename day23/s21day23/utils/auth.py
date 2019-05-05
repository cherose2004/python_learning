#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.base import BaseMiddlware
class AuthMiddleware(BaseMiddlware):
    def process(self,data):
        msg = "【auth】%s【auth】" % data
        return msg