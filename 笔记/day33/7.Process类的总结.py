#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Process类
# 开启进程的方式
    # 面向函数
        # def 函数名:要在子进程中执行的代码
        # p = Process(target= 函数名,args=(参数1，))
    # 面向对象
        # class 类名(Process):
            # def __init__(self,参数1，参数2):   # 如果子进程不需要参数可以不写
                # self.a = 参数1
                # self.b = 参数2
                # super().__init__()
            # def run(self):
                # 要在子进程中执行的代码
        # p = 类名(参数1，参数2)
    # Process提供的操作进程的方法
        # p.start() 开启进程      异步非阻塞
        # p.terminate() 结束进程  异步非阻塞

        # p.join()     同步阻塞
        # p.isalive()  获取当前进程的状态

        # daemon = True 设置为守护进程，守护进程永远在主进程的代码结束之后自动结束









