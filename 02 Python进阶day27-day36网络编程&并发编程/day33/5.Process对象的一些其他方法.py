#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 有一个参数可以把一个子进程设置为一个守护进程
import time
from multiprocessing import Process

def son1():
    while True:
        print('is alive')
        time.sleep(0.5)

if __name__ == '__main__':
    p = Process(target=son1)
    p.start()      # 异步 非阻塞
    print(p.is_alive())
    time.sleep(1)
    p.terminate()   # 异步的 非阻塞
    print(p.is_alive())   # 进程还活着 因为操作系统还没来得及关闭进程
    time.sleep(0.01)
    print(p.is_alive())   # 操作系统已经响应了我们要关闭进程的需求，再去检测的时候，得到的结果是进程已经结束了

# 什么是异步非阻塞？
    # terminate
