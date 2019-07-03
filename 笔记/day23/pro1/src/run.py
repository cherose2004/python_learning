#!/usr/bin/env python
# -*- coding:utf-8 -*-
from src import account
from src import order

def start():
    print('1.登陆；2.注册；3.订单管理')
    func_dict = {'1':account.login,'2':account.register,'3':order.manager}
    choice = input('选择')
    func = func_dict.get(choice)
    if not func:
        print('输入错误')
    func()