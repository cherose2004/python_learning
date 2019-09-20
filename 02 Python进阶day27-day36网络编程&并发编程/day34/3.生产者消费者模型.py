#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 解耦 ：修改 复用 可读性
# 把写在一起的大的功能分开成多个小的功能处理
# 登陆 注册

# 进程
    # 一个进程就是一个生产者
    # 一个进程就是一个消费者
# 队列
    # 生产者和消费者之间的容器就是队列
import time
import random
from multiprocessing import Process,Queue

def producer(q,name,food):
    for i in range(10):
        time.sleep(random.random())
        fd = '%s%s'%(food,i)
        q.put(fd)
        print('%s生产了一个%s'%(name,food))

def consumer(q,name):
    while True:
        food = q.get()
        if not food:break
        time.sleep(random.randint(1,3))
        print('%s吃了%s'%(name,food))


def cp(c_count,p_count):
    q = Queue(10)
    for i in range(c_count):
        Process(target=consumer, args=(q, 'alex')).start()
    p_l = []
    for i in range(p_count):
        p1 = Process(target=producer, args=(q, 'wusir', '泔水'))
        p1.start()
        p_l.append(p1)
    for p in p_l:p.join()
    for i in range(c_count):
        q.put(None)
if __name__ == '__main__':
    cp(2,3)






