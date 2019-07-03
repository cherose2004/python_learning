#!/usr/bin/env python
# -*- coding:utf-8 -*-

import demo
# from multiprocessing import Process
#
# def target(i):
#     print(i)
#
# if __name__ == '__main__':
#     p_l = []
#     for i in range(5):
#         p = Process(target=target,args=(i,))
#         p.start()
#         p_l.append(p)
#     # p.join()  # 阻塞 主进程 直到子进程执行完毕
#     for p in p_l:p.join()
#     print('子进程已经都执行完毕了')