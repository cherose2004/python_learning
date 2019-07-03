#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1.什么是GIL
    # 全局解释器锁
    # 由Cpython解释器提供的
    # 导致了一个进程中多个线程同一时刻只能有一个线程访问CPU
# 2.在进程、线程中都需要用到锁的概念
    # 互斥锁 在一个线程中不能连续acquire多次、效率高，产生死锁的几率大
    # 递归锁 在一个线程中可以连续acquire多次、效率低，一把锁永远不死锁
# 3.进程  开销大 数据隔离 能利用多核 数据不安全 操作系统控制
#   线程  开销中 数据共享 cpython解释器下不能利用多核 数据不安全 操作系统控制
#   协程  开销小 数据共享 不能利用多核 数据安全 用户控制
    # 在哪些地方用到了线程和协程
        # 1.自己用线程、协程完成爬虫任务
        # 2.但是后来有了比较丰富的爬虫框架
            # 了解到 scrapy /beautyful soup/aiogttp爬虫框架 哪些用到了线程，哪些用到了协程？
        # 3.web框架中的并发是如何实现的
            # 传统框架 ： django 多线程
            #             flask 优先选用协程 其次使用线程
            # socket server ：多线程
            # 异步框架 ：tornado，sanic底层都是协程
# 4.IPC 进程之间的通信机制
    # 内置的模块（基于文件） ：Pipe Queue
    # 第三方工具（基于网络）: redis rabbitmq kafaka memcache  发挥的都是消息中间件的功能
# 5.
# import gevent
# import requests
# from gevent import monkey
# monkey.patch_all()
#
# def get(url):
#     res = requests.get(url)
#     return res.text
# url_l = []
# g_l = []
# for url in url_l:
#     g = gevent.spawn(get,url)
#     g_l.append(g)
# gevent.joinall(g_l)
# for g in g_l:
#     print(g.value)


# 关于作业中的读代码
# 1.开启线程是几乎不需要事件的，start是一个异步非阻塞方法
# 2.对于整数的 += -= 来说 异步的多线程数据不安全，如果是同步的数据就安全了
# 3.对于列表的操作 无论是异步还是同步的 都是数据安全的


