#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Manager,Process,Lock

def func(dic,lock):
    with lock:
        dic['count'] -= 1

if __name__ == '__main__':
    # m = Manager()
    with Manager() as m:
        l = Lock()
        dic = m.dict({'count':100})
        p_l = []
        for i in range(100):
            p = Process(target=func,args=(dic,l))
            p.start()
            p_l.append(p)
        for p in p_l:p.join()
        print(dic)


# mulprocessing中有一个manager类
# 封装了所有和进程相关的 数据共享 数据传递
# 相关的数据类型
# 但是对于 字典 列表这一类的数据操作的时候会产生数据不安全
# 需要加锁解决问题，并且需要尽量少的使用这种方式









