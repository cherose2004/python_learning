#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 线程 开销小 数据共享 是进程的一部分
# 进程 开销大 数据隔离 是一个资源分配单位

# cpython解释器 不能实现多线程利用多核


# 锁 ：GIL 全局解释器锁
    # 保证了整个python程序中，只能有一个线程被CPU执行
    # 原因：cpython解释器中特殊的垃圾回收机制
    # GIL锁导致了线程不能并行，可以并发
# 所以使用所线程并不影响高io型的操作
# 只会对高计算型的程序由效率上的影响
# 遇到高计算 ： 多进程 + 多线程
              # 分布式

# cpython pypy jpython iron python

# 遇到IO操作的时候
    # 5亿条cpu指令/s
    # 5-6cpu指令 == 一句python代码
    # 几千万条python代码
# web框架 几乎都是多线程








