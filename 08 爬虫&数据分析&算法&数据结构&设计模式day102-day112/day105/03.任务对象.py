# -*- coding: utf-8 -*-
# __author__ = "maple"

from time import sleep
import asyncio

#回调函数:
#默认参数:任务对象
def callback(task):
    print('i am callback!!1')
    print(task.result())#result返回的就是任务对象对应的那个特殊函数的返回值

async def get_request(url):
    print('正在请求:',url)
    sleep(2)
    print('请求结束:',url)
    return 'hello bobo'

#创建一个协程对象
c = get_request('www.1.com')
#封装一个任务对象
task = asyncio.ensure_future(c)

#给任务对象绑定回调函数
task.add_done_callback(callback)

#创建一个事件循环对象
loop = asyncio.get_event_loop()
loop.run_until_complete(task)#将任务对象注册到事件循环对象中并且开启了事件循环
