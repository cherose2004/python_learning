#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 进程 资源分配的最小单位
# 线程 CPU执行的最小单位

# 只要是线程里的代码 就都被CPU执行就行
# 线程是由 操作系统 调度,由操作系统负责切换的
# 协程:
    # 用户级别的,由我们自己写的python代码来控制切换的
    # 是操作系统不可见的
# 在Cpython解释器下 - 协程和线程都不能利用多核,都是在一个CPU上轮流执行
    # 由于多线程本身就不能利用多核
    # 所以即便是开启了多个线程也只能轮流在一个CPU上执行
    # 协程如果把所有任务的IO操作都规避掉,只剩下需要使用CPU的操作
    # 就意味着协程就可以做到题高CPU利用率的效果
# 多线程和协程
    # 线程 切换需要操作系统,开销大,操作系统不可控,给操作系统的压力大
        # 操作系统对IO操作的感知更加灵敏
    # 协程 切换需要python代码,开销小,用户操作可控,完全不会增加操作系统的压力
        # 用户级别能够对IO操作的感知比较低








