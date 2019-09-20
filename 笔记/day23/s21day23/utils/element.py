#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.base import BaseMiddlware
class ElementMiddleware(BaseMiddlware):
    def process(self,data):
        return "element %s element" %(data,)