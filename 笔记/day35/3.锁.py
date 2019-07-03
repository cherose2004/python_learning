#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 线程中是不是会产生数据不安全
    # 共享内存
# a = 0
# def add_f():
#     global a
#     for i in range(200000):
#         a += 1
#
# def sub_f():
#     global a
#     for i in range(200000):
#         a -= 1

# from threading import Thread
#
# t1 = Thread(target=add_f)
# t1.start()
# t2 = Thread(target=sub_f)
# t2.start()
# t1.join()
# t2.join()
# print(a)
# a = 0
# def func():
#     global a
#     a -= 1
# import dis
# dis.dis(func)

# 即便是线程 即便有GIL 也会出现数据不安全的问题
    # 1.操作的是全局变量
    # 2.做一下操作
        # += -= *= /+ 先计算再赋值才容易出现数据不安全的问题
        # 包括 lst[0] += 1  dic['key']-=1

# a = 0
# def func():
#     global a
#     a += 1
#
# import dis
# dis.dis(func)


a = 0
def add_f(lock):
    global a
    for i in range(200000):
        with lock:
            a += 1

def sub_f(lock):
    global a
    for i in range(200000):
        with lock:
            a -= 1

# from threading import Thread,Lock
# lock = Lock()
# t1 = Thread(target=add_f,args=(lock,))
# t1.start()
# t2 = Thread(target=sub_f,args=(lock,))
# t2.start()
# t1.join()
# t2.join()
# print(a)
# 加锁会影响程序的执行效率，但是保证了数据的安全

# 互斥锁是锁中的一种:在同一个线程中，不能连续acquire多次
# from threading import Lock
# lock = Lock()
# lock.acquire()
# print('*'*20)
# lock.release()
# lock.acquire()
# print('-'*20)
# lock.release()
