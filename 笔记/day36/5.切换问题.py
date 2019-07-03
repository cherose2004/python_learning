#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 协程 :能够在一个线程下的多个任务之间来回切换,那么每一个任务都是一个协程
# 两种切换方式
    # 原生python完成   yield  asyncio
    # C语言完成的python模块  greenlet  gevent

# greenlet
# import time
# from  greenlet import greenlet
#
# def eat():
#     print('wusir is eating')
#     time.sleep(0.5)
#     g2.switch()
#     print('wusir finished eat')
#
# def sleep():
#     print('小马哥 is sleeping')
#     time.sleep(0.5)
#     print('小马哥 finished sleep')
#     g1.switch()
#
# g1 = greenlet(eat)
# g2 = greenlet(sleep)
# g1.switch()















