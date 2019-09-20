#!/usr/bin/env python
# -*- coding:utf-8 -*-

from threading import RLock
# rlock = RLock()
# rlock.acquire()
# print('*'*20)
# rlock.acquire()
# print('-'*20)
# rlock.acquire()
# print('*'*20)

# 在同一个线程中，可以连续acuqire多次不会被锁住

# 递归锁：
    # 好 ：在同一个进程中多次acquire也不会发生阻塞
    # 不好 ：占用了更多资源
import time
from threading import RLock,Thread
# noodle_lock = RLock()
# fork_lock = RLock()
noodle_lock = fork_lock = RLock()
print(noodle_lock,fork_lock)
def eat1(name,noodle_lock,fork_lock):
    noodle_lock.acquire()
    print('%s抢到面了'%name)
    fork_lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s吃了一口面'%name)
    time.sleep(0.1)
    fork_lock.release()
    print('%s放下叉子了' % name)
    noodle_lock.release()
    print('%s放下面了' % name)

def eat2(name,noodle_lock,fork_lock):
    fork_lock.acquire()
    print('%s抢到叉子了' % name)
    noodle_lock.acquire()
    print('%s抢到面了'%name)
    print('%s吃了一口面'%name)
    time.sleep(0.1)
    noodle_lock.release()
    print('%s放下面了' % name)
    fork_lock.release()
    print('%s放下叉子了' % name)

lst = ['alex','wusir','taibai','yuan']
Thread(target=eat1,args=(lst[0],noodle_lock,fork_lock)).start()
Thread(target=eat2,args=(lst[1],noodle_lock,fork_lock)).start()
Thread(target=eat1,args=(lst[2],noodle_lock,fork_lock)).start()
Thread(target=eat2,args=(lst[3],noodle_lock,fork_lock)).start()

