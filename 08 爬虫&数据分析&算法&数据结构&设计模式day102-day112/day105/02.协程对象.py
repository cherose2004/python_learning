# -*- coding: utf-8 -*-
# __author__ = "maple"

from time import sleep
import asyncio

async def get_request(url):
    print('正在请求:',url)
    sleep(2)
    print('请求结束:',url)

c = get_request('www.1.com')
print(c)