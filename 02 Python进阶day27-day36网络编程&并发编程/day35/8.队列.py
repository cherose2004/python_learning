#!/usr/bin/env python
# -*- coding:utf-8 -*-
import queue
# 线程之间的通信 线程安全
from queue import Queue  # 先进先出队列
# q = Queue(5)
# q.put(0)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print('444444')
#
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

# 使用多线程 实现一个请求网页 并且把网页写到文件中
# 生产者消费者模型来完成

# 5个线程负责请求网页 把结果放在队列里
# 2个线程 负责从队列中获取网页代码 写入文件

from queue import LifoQueue  # 后进先出队列
# last in first out 栈
# lfq = LifoQueue(4)
# lfq.put(1)
# lfq.put(3)
# lfq.put(2)
# print(lfq.get())
# print(lfq.get())
# print(lfq.get())

# 先进先出
    # 写一个server，所有的用户的请求放在队列里
        # 先来先服务的思想
# 后进先出
    # 算法
# 优先级队列
    # 自动的排序
    # 抢票的用户级别 100000 100001
    # 告警级别
# from queue import PriorityQueue
# pq = PriorityQueue()
# pq.put((10,'alex'))
# pq.put((6,'wusir'))
# pq.put((20,'yuan'))
# print(pq.get())
# print(pq.get())
# print(pq.get())