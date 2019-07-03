#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.base import BaseMiddlware
class SessionMiddleware(BaseMiddlware):
    def process(self,data):
        msg = "【session】%s【session】" %data
        return msg