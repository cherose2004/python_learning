#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from threading import Lock,Thread
lock = Lock()
def eat1(name,noodle_lock,fork_lock):
    lock.acquire()
    print('%s抢到面了'%name)
    print('%s抢到叉子了' % name)
    print('%s吃了一口面'%name)
    time.sleep(0.1)
    print('%s放下叉子了' % name)
    print('%s放下面了' % name)
    lock.release()

def eat2(name,noodle_lock,fork_lock):
    lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s抢到面了'%name)
    print('%s吃了一口面'%name)
    time.sleep(0.1)
    print('%s放下面了' % name)
    print('%s放下叉子了' % name)
    lock.release()

lst = ['alex','wusir','taibai','yuan']
Thread(target=eat1,args=(lst[0],noodle_lock,fork_lock)).start()
Thread(target=eat2,args=(lst[1],noodle_lock,fork_lock)).start()
Thread(target=eat1,args=(lst[2],noodle_lock,fork_lock)).start()
Thread(target=eat2,args=(lst[3],noodle_lock,fork_lock)).start()










