#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from threading import Thread
# multiprocessing 是完全仿照这threading的类写的
# def func():
#     print('start son thread')
#     time.sleep(1)
#     print('end son thread',os.getpid())
# # 启动线程 start
# Thread(target=func).start()
# print('start',os.getpid())
# time.sleep(0.5)
# print('end',os.getpid())

# 开启多个子线程
# def func(i):
#     print('start son thread',i)
#     time.sleep(1)
#     print('end son thread',i,os.getpid())
#
# for i in range(10):
#     Thread(target=func,args=(i,)).start()
# print('main')
# 主线程什么时候结束？等待所有子线程结束之后才结束
# 主线程如果结束了，主进程也就结束了

# join方法  阻塞 直到子线程执行结束
# def func(i):
#     print('start son thread',i)
#     time.sleep(1)
#     print('end son thread',i,os.getpid())
# t_l = []
# for i in range(10):
#     t = Thread(target=func,args=(i,))
#     t.start()
#     t_l.append(t)
# for t in t_l:t.join()
# print('子线程执行完毕')

# 使用面向对象的方式启动线程
# class MyThread(Thread):
#     def __init__(self,i):
#         self.i = i
#         super().__init__()
#     def run(self):
#         print('start',self.i,self.ident)
#         time.sleep(1)
#         print('end',self.i)
#
# for i in range(10):
#     t = MyThread(i)
#     t.start()
#     print(t.ident)

# 线程里的一些其他方法
# from threading import current_thread,enumerate,active_count
# def func(i):
#     t = current_thread()
#     print('start son thread',i,t.ident)
#     time.sleep(1)
#     print('end son thread',i,os.getpid())
#
# t = Thread(target=func,args=(1,))
# t.start()
# print(t.ident)
# print(current_thread().ident)   # 水性杨花 在哪一个线程里，current_thread()得到的就是这个当前线程的信息
# print(enumerate())
# print(active_count())   # =====len(enumerate())

# terminate 结束进程
# 在线程中不能从主线程结束一个子线程

# 测试
    # 进程和线程的效率差
# def func(a,b):
#     c = a+b
# import time
# from multiprocessing import Process
# from threading import Thread
# if __name__ == '__main__':
#     start = time.time()
#     p_l = []
#     for  i in range(500):
#         p = Process(target=func,args=(i,i*2))
#         p.start()
#         p_l.append(p)
#     for p in p_l:p.join()
#     print('process :',time.time() - start)
#
#     start = time.time()
#     p_l = []
#     for i in range(500):
#         p = Thread(target=func, args=(i, i * 2))
#         p.start()
#         p_l.append(p)
#     for p in p_l: p.join()
#     print('thread :',time.time() - start)

    # 数据隔离还是共享？
# from threading import Thread
# n = 100
# def func():
#     global n    # 不要在子线程里随便修改全局变量
#     n-=1
# t_l = []
# for i in range(100):
#     t = Thread(target=func)
#     t_l.append(t)
#     t.start()
# for t in t_l:t.join()
# print(n)

# 守护线程
# import time
# from threading import Thread
# def son1():
#     while True:
#         time.sleep(0.5)
#         print('in son1')
# def son2():
#     for i in range(5):
#         time.sleep(1)
#         print('in son2')
# t =Thread(target=son1)
# t.daemon = True
# t.start()
# Thread(target=son2).start()
# time.sleep(3)
# 守护线程一直等到所有的非守护线程都结束之后才结束
# 除了守护了主线程的代码之外也会守护子线程
# 小绿本 ：p38 ：34题
