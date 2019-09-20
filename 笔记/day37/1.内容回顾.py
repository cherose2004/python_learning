#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 协程
    # 协程的基础概念
        # 什么是协程：多个任务在一条线程上来回切换
        # 我们写协程 ：在一条线程上最大限度的提高CPU的使用率，
                    # 在一个任务中遇到IO的时候就切换到其他任务
        # 协程的特点：
            # 开销很小，是用户级的（只能感知从用户级别能够感知的IO操作），
            # 不能利用多核，数据共享，数据安全
    # 模块和用法
        # gevent    基于greenlet切换
            # 先导入模块
            # 导入monkey，执行patch all
            # 写一个函数当作协程要执行的任务
            # 协程对象 = gevent.spawn(函数名,参数，)
            # 协程对象.join()，gevent.joinall([g1,g2...])

            # 分辨gevent是否识别了我们写的代码中的io操作的方法
                # 再patchall之前打印一下涉及到io操作的函数地址
                # 再patchall之后打印一下涉及到io操作的函数地址
                # 如果两个地址一致，说明gevent没有识别这个io，如果不一致说明识别了
        # asyncio   基于yield机制切换的
            # async 标识一个协程函数
            # await 后面跟着一个asyncio模块提供的io操作的函数
            # loop  事件循环，负责在多个任务之间进行切换的
            # 最简单的协程函数是如何完成的
# import asyncio
#
# async def func():
#     print('start')
#     await asyncio.sleep(1)
#     print('end')
#
# loop = asyncio.get_event_loop()
# # loop.run_until_complete(func())
# wait_l = asyncio.wait([func(),func()])
# loop.run_until_complete(wait_l)