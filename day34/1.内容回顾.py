#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 关于默写和抄写
# 关于作业的回复
    # 登陆认证 + 上传下载
        # 周五讲解的那一版本 登陆+上传下载
    # ftp作业
        # 1%   5%
        # 周末作业  1-4个需求
    # 计算器

# tcp协议是可靠还是安全
    # tcp ： 可靠
    # https ：安全

# 还没有明白并发和并行的区别
    # 单核 并发
    # 多核 多个程序跑在多个cpu上，在同一时刻 并行
    # 10个进程 ：
        # 可以利用多核  并行
        # 也有并发的成分
# 进程是计算机中最小的资源分配单位
# 线程是计算机中最小的被CPU调度的单位
# 8核/4核8线程

# 使用进程实现并发的socket的server端

# 生成器的题
    # 取一次就没有了
    # 惰性运算 ：不取不执行


# [0,1,2,3,4,5,6,7,8,9]
# ret = filter(lambda n:n%3==0,range(10))
# # ret是迭代器
# print(len(list(ret)))   # 4
# print(len(list(ret)))   # 0

# def demo():
#     for i in range(4):
#         yield i
# g=demo()
# g1=(i for i in g)
# g2=(i for i in g1)
# print(list(g))
# print(list(g1))
# print(list(g2))

# def add(n,i):
#     return n+i
# def test():
#     for i in range(4):
#         yield i
# g=test()
# for n in [1,10,5]:
#     g=(add(n,i) for i in g)
# print(list(g))