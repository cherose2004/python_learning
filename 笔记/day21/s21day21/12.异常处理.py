#!/usr/bin/env python
# -*- coding:utf-8 -*-

def func():
    result = True
    try:
        with open('x.log',mode='r',encoding='utf-8') as f:
            data = f.read()
        if 'alex' not in data:
            raise Exception()
    except Exception as e:
        result = False
    return result