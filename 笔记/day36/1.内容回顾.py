#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 1.增加了面试环节
    # 函数 模块
    # 并发 数据库
    # 每一个项目 答辩
# 2.后期的项目
    # 多写 自己写 自己理解流程
from threading import Lock
# 锁 - 都可以维护线程之间的数据安全
    # 互斥锁 ：一把锁不能在一个线程中连续acquire，开销小
    # 递归锁 ：一把锁可以连续在一个线程中acquire多次，acquire多少次就release多少次，开销大

    # 死锁现象
        # 在某一些线程中出现陷入阻塞并且永远无法结束阻塞的情况就是死锁现象
        # 出现死锁：
            # 多把锁+交替使用
            # 互斥锁在一个线程中连续acquire
    # 避免死锁
        # 在一个线程中只有一把锁，并且每一次acquire之后都要release

    # += -= *= /= ，多个线程对同一个文件进行写操作

# 队列
    # 先进先出 Queue
    # 后进先出 LifoQueue
    # 优先级   PriorityQueue
# 池
    # from concurrent.futrues import ThreadPoolExecutor
    # 1.是单独开启线程进程还是池？
        # 如果只是开启一个子线程做一件事情，就可以单独开线程
        # 有大量的任务等待程序去做，要达到一定的并发数，开启线程池
        # 根据你程序的io操作也可以判定是用池还是不用池？
            # socket的server 大量的阻塞io   recv recvfrom socketserver
            # 爬虫的时候 池
    # 2.回调函数add_done_callback
            # 执行完子线程任务之后直接调用对应的回调函数
            # 爬取网页 需要等待数据传输和网络上的响应高IO的 -- 子线程
            # 分析网页 没有什么IO操作 -- 这个操作没必要在子线程完成，交给回调函数
    # 3.ThreadPoolExecutor中的几个常用方法
        # tp = ThreadPoolExecutor(cpu*5)
        # obj = tp.submit(需要在子线程执行的函数名,参数)
        # obj
            # 1.获取返回值 obj.result() 是一个阻塞方法
            # 2.绑定回调函数 obj.add_done_callback(子线程执行完毕之后要执行的代码对应的函数)
        # ret = tp.map(需要在子线程执行的函数名,iterable)
            # 1.迭代ret，总是能得到所有的返回值
        # shutdown
            # tp.shutdown()

# 进程 和 线程都有锁
    # 所有在线程中能工作的基本都不能在进程中工作
    # 在进程中能够使用的基本在线程中也可以使用


# import time
# from concurrent.futures import ThreadPoolExecutor
# def son():
#     print(123)
#     time.sleep(3)
#     return 123
# def call_back(num):
#     print(num.result())
# t = ThreadPoolExecutor(20)
# obj = t.submit(son)
# print('main ： ',obj)
# obj.add_done_callback(call_back)


# 在多进程里启动多线程
# import os
# from multiprocessing import Process
# from threading import Thread
#
# def tfunc():
#     print(os.getpid())
# def pfunc():
#     print('pfunc-->',os.getpid())
#     Thread(target=tfunc).start()
#
# if __name__ == '__main__':
#     Process(target=pfunc).start()








