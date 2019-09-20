#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 每天的做事流程
# 大概需要多久
    # 1个小时 整理笔记
    # 1个小时 被概念和写例子
    # 1个小时 ftp作业
    # 1个小时 预习
# 默写
    # 把每天的默写总结下来 隔段（不要超过一周）时间进行复习
# 进程
    # Queue
        # 生产者消费者模型
    # JoinableQueue
        # 生产者消费者模型
    # 什么是生产者消费者模型
        # 把一个产生数据并且处理数据的过程解耦
        # 让生产的数据的过程和处理数据的过程达到一个工作效率上的平衡
        # 中间的容器，在多进程中我们使用队列或者可被join的队列，做到控制数据的量
            # 当数据过剩的时候，队列的大小会控制这生产者的行为
            # 当数据严重不足的时候，队列会控制消费者的行为
            # 并且我们还可以通过定期检查队列中元素的个数来调节生产者消费者的个数
        # 比如说：一个爬虫，或者一个web程序的server端
            # 爬虫
                # 请求网页的平均时间是0.3s
                # 处理网页代码的时候是0.003s
                # 100倍，每启动100个线程生产数据
                # 启动一个线程来完成处理数据
            # web程序的server端
                # 每秒钟有6w条请求
                    # 一个服务每s中只能处理2000条
                    # 先写一个web程序，只负责一件事情，就是接收请求，然后把请求放到队列中
                    # 再写很多个server端，从队列中获取请求，然后处理，然后返回结果
# 线程
    # 线程：开销小 数据共享 是进程的一部分，不能独立存在 本身可以利用多核
    # GIL锁
        # 全局解释器锁
        # cpython解释器中的机制
        # 导致了在同一个进程中多个线程不能同时利用多核 —— python的多线程只能是并发不能是并行
    # threading模块
        # 创建线程 ：面向函数 面向对象
        # 线程中的几个方法：
            # 属于线程对象t.start(),t.join()
            # 守护线程t.daemon = True 等待所有的非守护子线程都结束之后才结束
                # 非守护线程不结束，主线程也不结束
                # 主线程结束了，主进程也结束
                # 结束顺序 ：非守护线程结束 -->主线程结束-->主进程结束
                            #-->主进程结束 --> 守护线程也结束
            # threading模块的函数 ：
                # current_thread 在哪个线程中被调用，就返回当前线程的对象
                # 活着的线程，包括主线程
                    # enumerate 返回当前活着的线程的对象列表
                    # active_count 返回当前或者的线程的个数
            # 测试
                # 进程和线程的效率差，线程的开启、关闭、切换效率更高
                # 线程的数据共享的效果
# 操作系统
    # 多道 遇到io会切换
    # 分时 时间片到了会切换
# 进程的重点
    # 进程的特点 ：
        # 数据隔离  IPC
        # 开销大
        # 能利用多核
        # 进程之间共享数据的安全问题：Lock
# 生产者消费者模型

# g1 = filter(lambda n:n%2==0,range(10))   # g1 = [0,2,4,6,8]
# g2 = map(lambda n:n*2,range(3))          # g2 = [0,2,4]
# for i in g1:
#     for j in g2:
#         print(i*j)

# def multipliers():
#     return (lambda x:i*x for i in range(4))
# print([m(2) for m in multipliers()])

# 生成器函数
# 生成器
# for循环 + lambda


