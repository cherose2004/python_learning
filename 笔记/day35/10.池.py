#!/usr/bin/env python
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

# 池
    # 进程池
    # 线程池
# 为什么要有池？
# 10000
# 池
# 预先的开启固定个数的进程数，当任务来临的时候，直接提交给已经开好的进程
# 让这个进程去执行就可以了
# 节省了进程，线程的开启 关闭 切换都需要时间
# 并且减轻了操作系统调度的负担

# concurrent.futures
import os
import time
import random
from concurrent.futures import ProcessPoolExecutor
# submit + shutdown
# def func():
#     print('start',os.getpid())
#     time.sleep(random.randint(1,3))
#     print('end', os.getpid())
# if __name__ == '__main__':
#     p = ProcessPoolExecutor(5)
#     for i in range(10):
#         p.submit(func)
#     p.shutdown()   # 关闭池之后就不能继续提交任务，并且会阻塞，直到已经提交的任务完成
#     print('main',os.getpid())

# 任务的参数 + 返回值
# def func(i,name):
#     print('start',os.getpid())
#     time.sleep(random.randint(1,3))
#     print('end', os.getpid())
#     return '%s * %s'%(i,os.getpid())
# if __name__ == '__main__':
#     p = ProcessPoolExecutor(5)
#     ret_l = []
#     for i in range(10):
#         ret = p.submit(func,i,'alex')
#         ret_l.append(ret)
#     for ret in ret_l:
#         print('ret-->',ret.result())  # ret.result() 同步阻塞
#     print('main',os.getpid())

# 开销大
# 一个池中的任务个数限制了我们程序的并发个数

# 线程池
# from concurrent.futures import ThreadPoolExecutor
# def func(i):
#     print('start', os.getpid())
#     time.sleep(random.randint(1,3))
#     print('end', os.getpid())
#     return '%s * %s'%(i,os.getpid())
# tp = ThreadPoolExecutor(20)
# ret_l = []
# for i in range(10):
#     ret = tp.submit(func,i)
#     ret_l.append(ret)
# tp.shutdown()
# print('main')
# for ret in ret_l:
#     print('------>',ret.result())



# from concurrent.futures import ThreadPoolExecutor
# def func(i):
#     print('start', os.getpid())
#     time.sleep(random.randint(1,3))
#     print('end', os.getpid())
#     return '%s * %s'%(i,os.getpid())
# tp = ThreadPoolExecutor(20)
# ret = tp.map(func,range(20))
# for i in ret:
#     print(i)
# ret_l = []
# for i in range(10):
#     ret = tp.submit(func,i)
#     ret_l.append(ret)
# tp.shutdown()
# print('main')

# 回调函数
import requests
from concurrent.futures import ThreadPoolExecutor
def get_page(url):
    res = requests.get(url)
    return {'url':url,'content':res.text}

def parserpage(ret):
    dic = ret.result()
    print(dic['url'])
tp = ThreadPoolExecutor(5)
url_lst = [
    'http://www.baidu.com',   # 3
    'http://www.cnblogs.com', # 1
    'http://www.douban.com',  # 1
    'http://www.tencent.com',
    'http://www.cnblogs.com/Eva-J/articles/8306047.html',
    'http://www.cnblogs.com/Eva-J/articles/7206498.html',
]
ret_l = []
for url in url_lst:
    ret = tp.submit(get_page,url)
    ret_l.append(ret)
    ret.add_done_callback(parserpage)


# ThreadPoolExcutor
# ProcessPoolExcutor

# 创建一个池子
# tp = ThreadPoolExcutor(池中线程/进程的个数)
# 异步提交任务
# ret = tp.submit(函数,参数1，参数2....)
# 获取返回值
# ret.result()
# 在异步的执行完所有任务之后，主线程/主进程才开始执行的代码
# tp.shutdown() 阻塞 直到所有的任务都执行完毕
# map方法
# ret = tp.map(func,iterable) 迭代获取iterable中的内容，作为func的参数，让子线程来执行对应的任务
# for i in ret: 每一个都是任务的返回值
# 回调函数
# ret.add_done_callback(函数名)
# 要在ret对应的任务执行完毕之后，直接继续执行add_done_callback绑定的函数中的内容，并且ret的结果会作为参数返回给绑定的函数

# 5个进程
# 20个线程
# 5*20 = 100个并发





