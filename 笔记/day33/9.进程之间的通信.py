#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 进程之间的数据隔离
# from multiprocessing import Process
# n = 100
# def func():
#     global n
#     n -= 1
#
# if __name__ == '__main__':
#     p_l = []
#     for i in range(10):
#         p = Process(target=func)
#         p.start()
#         p_l.append(p)
#     for p in p_l:p.join()
#     print(n)


# 通信
# 进程之间的通信 - IPC（inter process communication）
# from multiprocessing import Queue,Process
# # 先进先出
# def func(exp,q):
#     ret = eval(exp)
#     q.put({ret,2,3})
#     q.put(ret*2)
#     q.put(ret*4)
#
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=func,args=('1+2+3',q)).start()
#     print(q.get())
#     print(q.get())
#     print(q.get())

# Queue基于 天生就是数据安全的
    # 文件家族的socket pickle lock
# pipe 管道(不安全的) = 文件家族的socket pickle
# 队列 = 管道 + 锁
# from multiprocessing import Pipe
# pip = Pipe()
# pip.send()
# pip.recv()
import queue

# from multiprocessing import Queue
# q = Queue(5)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)   # 当队列为满的时候再向队列中放数据 队列会阻塞
# print('5555555')
# try:
#     q.put_nowait(6)  # 当队列为满的时候再向队列中放数据 会报错并且会丢失数据
# except queue.Full:
#     pass
# print('6666666')
#
# print(q.get())
# print(q.get())
# print(q.get())   # 在队列为空的时候会发生阻塞
# print(q.get())   # 在队列为空的时候会发生阻塞
# print(q.get())   # 在队列为空的时候会发生阻塞
# try:
#     print(q.get_nowait())   # 在队列为空的时候 直接报错
# except queue.Empty:pass


# 队列
# 生产者消费者模型


# 笔记的整理 两天
# 作业
# 整理考试题
# 估分



















