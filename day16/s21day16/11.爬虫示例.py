#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


session = requests.Session()
i1 = session.get(url="http://dig.chouti.com/help/service", headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'})
i2 = session.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': "86手机号",
        'password': "密码",
        'oneMonth': ""
    },
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
)
i3 = session.post(
    url="http://dig.chouti.com/link/vote?linksId=25723176",
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
)
print(i3.text)
