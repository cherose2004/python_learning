# -*- coding: utf-8 -*-
# __author__ = "maple"

# 概念
    # 知识点：
        # 操作系统原理
            # 发展历程 进程-->线程-->协程
                # 所有的程序运行的过程、硬件的调度都是由操作系统控制
                # 分配资源 运行代码
        # 进程 负责圈资源的
            # 资源分配的最小单位
            # 进程之间是数据隔离的
            # 进程是需要操作系调度的
            # 可以利用多核
            # 创建和销毁占用大量的资源
            # 进程的三状态图 ： 就绪 运行(CPU) 阻塞(IO)
        # IPC机制 进程之间通信
            # 管道 队列 socket网络
            # 第三方消息中间件 ：redis rabbitmq kafka
        # IO操作
            # 文件操作(网络请求 input print) sleep
            # 输入 ：向内存输入 原本内存中没有 现在有了
            # 输出 ：原本内存中存在 通过其他的渠道输出到内存外
        # 线程 ：开销小 数据不隔离
            # 线程被称为轻量级 轻型进程
            # 每个线程可以帮助程序规避一些IO操作
            # 线程本身可以利用多核
            # 线程由操作系统调度
            # Cpython解释器下 GIL 全局解释器锁
                # 导致了多个线程在一个进程中同一时刻只能一个线程访问CPU调度
                # 起线程能极大的减少IO操作的时间
        # 协程 :
            # 不占用操作系统调度的时间、用户级别的
            # 本质就是一条线程
            # 不能同时使用多核
            # 协程对于IO操作的感应是非常薄弱的（只能感受到网络操作的IO）
        # 正确的并发机制：
            # 线程20+协程
        # 锁：
            # 互斥锁 lock  容易造成死锁   效率高
            # 递归锁 rlock 不容易发生死锁 占用资源
        # 死锁现象 - 多把锁交替使用
    # 面试的问题
        # 1.什么是进程 线程 协程
        # 2.线程和协程的区别
        # 3.GIL锁 -cpython
        # 4.哪些地方用过进程 ：用过 试过
        # 5.哪些地方用过线程 ：django、flask框架、爬虫
        # 6.哪些地方用过协程 ：flask、sanic框架、爬虫
        # 7.你为什么要用爬虫？ ： 项目需要 朋友需要 自己需要 公司需要
        # 8.C10k C10M
            # connection 10 *1000 = 10000连接
            # 线程(20) * 协程(500)

            # connection 10 * 1000 * 1000 = 10000000并发
            # nginx  负载均衡
            # haproxy 负载均衡
        # 9.xxxx是不是线程安全的？
            # 列表、字典 pop extend append  线程安全的
            # 列表[0] +=1  字典[key] += 1 线程不安全
            # queue 安全
            # logging模块是线程安全
# 代码
    # 进程
        # multiprocessing
            # Process
            # Queue\Pipe
            # Lock\Rlock
    # 线程
        # threading
            # Thread
            # Lock、Rlock
        # queue
            # 数据安全的
    # 协程
        # gevent
        # asyncio ： async func():pass
        # aiohttp
    # 池
        # concurrent.futrues
            # ProcessPoolExcutor
            # ThreadPoolExcutor







