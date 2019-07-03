#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 操作系统
    # 1.计算机中所有的资源都是由操作系统分配的
    # 2.操作系统调度任务：时间分片、多道机制
    # 3.CPU的利用率是我们努力的指标
# 并发
    # 进程 开销大 数据隔离 资源分配单位 cpython下可以利用多核
        # 进程的三状态：就绪 运行 阻塞
        # multiprocessing模块
            # Process-开启进程
            # Lock - 互斥锁
                # 为什么要在进程中加锁
                    # 因为进程操作文件也会发生数据不安全
            # Queue -队列 IPC机制（Pipe,redis,memcache,rabbitmq,kafka）
                # 生产者消费者模型
            # Manager - 提供数据共享机制
    # 线程 开销小 数据共享 cpu调度单位  cpython下不能利用多核
        # GIL锁
            # 全局解释器锁
            # Cpython解释器提供的
            # 导致了一个进程中多个线程同一时刻只有一个线程能当问CPU -- 多线程不能利用多核
        # threading
            # Thread类 - 能开启线程start，等待线程结束join
            # Lock-互斥锁  不能在一个线程中连续acquire，效率相对高
            # Rlock-递归锁  可以在一个线程中连续acquire，效率相对低
            # 死锁现象如何发生?如何避免？
        # 线程队列 queue模块
            # Queue
            # LifoQueue
            # PriorityQueue
    # 池
        # concurrent.futrues.ThreadPoolExecutor,ProcessPoolExecutor
            # 实例化一个池 tp = ThreadPoolExecutor(num),pp = ProcessPoolExecutor(num)
            # 提交任务到池中，返回一个对象 obj = tp.submit(func,arg1,arg2...)
                # 使用这个对象获取返回值 obj.result()
                # 回调函数 obj.add_done_callback(函调函数)
            # 阻塞等待池中的任务都结束 tp.shutdown()
# 概念
    # IO操作
    # 同步异步
    # 阻塞非阻塞

# 1.所有讲过的概念都记住
# 2.数据安全问题
# 3.数据隔离和通信
# 4.会用基本的进程 线程 池