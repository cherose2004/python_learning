#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio

# 起一个任务
# async def demo():   # 协程方法
#     print('start')
#     await asyncio.sleep(1)  # 阻塞
#     print('end')
#
# loop = asyncio.get_event_loop()  # 创建一个事件循环
# loop.run_until_complete(demo())  # 把demo任务丢到事件循环中去执行

# 启动多个任务,并且没有返回值
# async def demo():   # 协程方法
#     print('start')
#     await asyncio.sleep(1)  # 阻塞
#     print('end')
#
# loop = asyncio.get_event_loop()  # 创建一个事件循环
# wait_obj = asyncio.wait([demo(),demo(),demo()])
# loop.run_until_complete(wait_obj)

# 启动多个任务并且有返回值
# async def demo():   # 协程方法
#     print('start')
#     await asyncio.sleep(1)  # 阻塞
#     print('end')
#     return 123
#
# loop = asyncio.get_event_loop()
# t1 = loop.create_task(demo())
# t2 = loop.create_task(demo())
# tasks = [t1,t2]
# wait_obj = asyncio.wait([t1,t2])
# loop.run_until_complete(wait_obj)
# for t in tasks:
#     print(t.result())

# 谁先回来先取谁的结果
# import asyncio
# async def demo(i):   # 协程方法
#     print('start')
#     await asyncio.sleep(10-i)  # 阻塞
#     print('end')
#     return i,123
#
# async def main():
#     task_l = []
#     for i in range(10):
#         task = asyncio.ensure_future(demo(i))
#         task_l.append(task)
#     for ret in asyncio.as_completed(task_l):
#         res = await ret
#         print(res)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())



# import asyncio
#
# async def get_url():
#     reader,writer = await asyncio.open_connection('www.baidu.com',80)
#     writer.write(b'GET / HTTP/1.1\r\nHOST:www.baidu.com\r\nConnection:close\r\n\r\n')
#     all_lines = []
#     async for line in reader:
#         data = line.decode()
#         all_lines.append(data)
#     html = '\n'.join(all_lines)
#     return html
#
# async def main():
#     tasks = []
#     for url in range(20):
#         tasks.append(asyncio.ensure_future(get_url()))
#     for res in asyncio.as_completed(tasks):
#         result = await res
#         print(result)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())  # 处理一个任务


# python原生的底层的协程模块
    # 爬虫 webserver框架
    # 题高网络编程的效率和并发效果
# 语法
    # await 阻塞 协程函数这里要切换出去，还能保证一会儿再切回来
    # await 必须写在async函数里，async函数是协程函数
    # loop 事件循环
    # 所有的协程的执行 调度 都离不开这个loop