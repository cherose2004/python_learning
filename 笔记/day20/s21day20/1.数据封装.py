#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask

class Request:
    def __init__(self,a1,a2,a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

def func(arg):
    arg.a1
    arg.a2
    arg.a3


obj = Request(1,2,3)
func(obj)