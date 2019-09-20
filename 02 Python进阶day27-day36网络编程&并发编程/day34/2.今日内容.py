#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 什么是io操作
    # i input  向内存输入  input read recv recvftom accept connect close
    # o output 从内存输出  print write send sendto accept connect close
# start terminate join
    # start terminate   异步 非阻塞
    # join   同步阻塞
# ipc，常见的ipc机制
    # 进程之间通信
    # ipc机制 ：队列 管道
    # 第三方工具（软件）提供给我们的IPC机制
        # redis
        # memcache
        # kafka
        # rabbitmq

        # 并发需求
        # 高可用
        # 断电保存数据
        # 解耦

# 5个进程 p1-p5,p1,p2,结束之后p3-p5才开始,p3必须随着p4\p5结束
# from multiprocessing import Process
# def func():
#     pass
# if __name__ == '__main__':
#     p1 = Process(target=func)
#     p2 = Process(target=func)
#     p3 = Process(target=func)
#     p4 = Process(target=func)
#     p5 = Process(target=func)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     p3.daemon = True
#     p3.start()
#     p4.start()
#     p5.start()
#     p4.join()
#     p5.join()

# 生产者消费者模型（****）
# 进程之间的数据共享（*）
# 初识线程
    # cpython解释器当中的线程问题（*****）
# python操作线程（*****）
    # 代码





