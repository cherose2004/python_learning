#!/usr/bin/env python
# -*- coding:utf-8 -*-

import getpass

pwd = getpass.getpass('请输入密码：')
if pwd == '123':
    print('输入正确')