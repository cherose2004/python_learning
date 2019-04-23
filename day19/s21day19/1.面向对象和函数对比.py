#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 封装思想：将同一类的函数封装到了同一个py文件中，以后方便使用。
from src import account

account.login()
account.logout()
account.register()