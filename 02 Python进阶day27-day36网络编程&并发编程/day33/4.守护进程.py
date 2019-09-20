#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 有一个参数可以把一个子进程设置为一个守护进程
import time
from multiprocessing import Process

def son1(a,b):
    while True:
        print('is alive')
        time.sleep(0.5)

def son2():
    for i in range(5):
        print('in son2')
        time.sleep(1)

if __name__ == '__main__':
    p = Process(target=son1,args=(1,2))
    p.daemon = True
    p.start()      # 把p子进程设置成了一个守护进程
    p2 = Process(target=son2)
    p2.start()
    time.sleep(2)

# 守护进程是随着主进程的代码结束而结束的
    # 生产者消费者模型的时候
    # 和守护线程做对比的时候
# 所有的子进程都必须在主进程结束之前结束，由主进程来负责回收资源