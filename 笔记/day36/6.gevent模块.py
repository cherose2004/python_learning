#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import time
# print('-->',time.sleep)
# import gevent
# from gevent import monkey
# monkey.patch_all()
# def eat():
#     print('wusir is eating')
#     print('in eat: ',time.sleep)
#     time.sleep(1)
#     print('wusir finished eat')
#
# def sleep():
#     print('小马哥 is sleeping')
#     time.sleep(1)
#     print('小马哥 finished sleep')
#
# g1 = gevent.spawn(eat)  # 创造一个协程任务
# g2 = gevent.spawn(sleep)  # 创造一个协程任务
# g1.join()   # 阻塞 直到g1任务完成为止
# g2.join()   # 阻塞 直到g1任务完成为止


# import time
# import gevent
# from gevent import monkey
# monkey.patch_all()
# def eat():
#     print('wusir is eating')
#     time.sleep(1)
#     print('wusir finished eat')
#
# def sleep():
#     print('小马哥 is sleeping')
#     time.sleep(1)
#     print('小马哥 finished sleep')
#
# # g1 = gevent.spawn(eat)  # 创造一个协程任务
# # g3 = gevent.spawn(eat)  # 创造一个协程任务
# # g2 = gevent.spawn(sleep)  # 创造一个协程任务
# # # g1.join()   # 阻塞 直到g1任务完成为止
# # # g2.join()   # 阻塞 直到g1任务完成为止
# # gevent.joinall([g1,g2,g3])
# g_l = []
# for i in range(10):
#     g = gevent.spawn(eat)
#     g_l.append(g)
# gevent.joinall(g_l)

# import time
# import gevent
# from gevent import monkey
# monkey.patch_all()
# def eat():
#     print('wusir is eating')
#     time.sleep(1)
#     print('wusir finished eat')
#     return 'wusir***'
#
# def sleep():
#     print('小马哥 is sleeping')
#     time.sleep(1)
#     print('小马哥 finished sleep')
#     return '小马哥666'
#
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(sleep)
# gevent.joinall([g1,g2])
# print(g1.value)
# print(g2.value)