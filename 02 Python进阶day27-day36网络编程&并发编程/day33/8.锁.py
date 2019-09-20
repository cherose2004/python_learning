#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 并发 能够做的事儿
# 1.实现能够响应多个client端的server
# 2.抢票系统
import time
import json
from multiprocessing import Process,Lock

def search_ticket(user):
    with open('ticket_count') as f:
        dic = json.load(f)
        print('%s查询结果  : %s张余票'%(user,dic['count']))

def buy_ticket(user,lock):
    # with lock:
    # lock.acquire()   # 给这段代码加上一把锁
        time.sleep(0.02)
        with open('ticket_count') as f:
            dic = json.load(f)
        if dic['count'] > 0:
            print('%s买到票了'%(user))
            dic['count'] -= 1
        else:
            print('%s没买到票' % (user))
        time.sleep(0.02)
        with open('ticket_count','w') as f:
            json.dump(dic,f)
    # lock.release()   # 给这段代码解锁

def task(user, lock):
    search_ticket(user)
    with lock:
        buy_ticket(user, lock)

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=task,args=('user%s'%i,lock))
        p.start()


# 1.如果在一个并发的场景下，涉及到某部分内容
    # 是需要修改一些所有进程共享数据资源
    # 需要加锁来维护数据的安全
# 2.在数据安全的基础上，才考虑效率问题
# 3.同步存在的意义
    # 数据的安全性

# 在主进程中实例化 lock = Lock()
# 把这把锁传递给子进程
# 在子进程中 对需要加锁的代码 进行 with lock：
    # with lock相当于lock.acquire()和lock.release()
# 在进程中需要加锁的场景
    # 共享的数据资源（文件、数据库）
    # 对资源进行修改、删除操作
# 加锁之后能够保证数据的安全性 但是也降低了程序的执行效率



























