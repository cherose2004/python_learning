#!/usr/bin/env python
# -*- coding:utf-8 -*-

# multi   multiple 多元的
# processing 进程
# import os
# import time
# print('start')
# time.sleep(20)
# print(os.getpid(),os.getppid(),'end')

# pid   process id
# ppid  parent process id

# 子进程
# 父进程 在父进程中创建子进程
# 在pycharm中启动的所有py程序都是pycharm的子进程
# import os
# import time
# from multiprocessing import Process
#
# def func():
#     print('start',os.getpid())
#     time.sleep(1)
#     print('end',os.getpid())
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()   # 异步 调用开启进程的方法 但是并不等待这个进程真的开启
#     print('main :',os.getpid())

# import os
# import time
# from multiprocessing import Process
#
# def eat():
#     print('start eating',os.getpid())
#     time.sleep(1)
#     print('end eating',os.getpid())
#
# def sleep():
#     print('start sleeping',os.getpid())
#     time.sleep(1)
#     print('end sleeping',os.getpid())
#
# if __name__ == '__main__':
#     p1 = Process(target=eat)    # 创建一个即将要执行eat函数的进程对象
#     p1.start()                  # 开启一个进程
#     p2 = Process(target=sleep)  # 创建一个即将要执行sleep函数的进程对象
#     p2.start()                  # 开启进程
#     print('main :',os.getpid())


# import os
# import time
# from multiprocessing import Process
# def func():
#     print('start',os.getpid())
#     time.sleep(1)
#     print('end',os.getpid())
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()   # 异步 调用开启进程的方法 但是并不等待这个进程真的开启
#     print('main :',os.getpid())

# 操作系统创建进程的方式不同
# windows操作系统执行开启进程的代码
    # 实际上新的子进程需要通过import父进程的代码来完成数据的导入工作
    # 所以有一些内容我们只希望在父进程中完成，就写在if __name__ == '__main__':下面
# ios linux操作系统创建进程 fork

# 主进程和子进程之间的关系
# import os
# import time
# from multiprocessing import Process
# def func():
#     print('start',os.getpid())
#     time.sleep(10)
#     print('end',os.getpid())
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()   # 异步 调用开启进程的方法 但是并不等待这个进程真的开启
#     print('main :',os.getpid())
    # 主进程没结束 ：等待子进程结束
    # 主进程负责回收子进程的资源
    # 如果子进程执行结束，父进程没有回收资源，那么这个子进程会变成一个僵尸进程

    # 主进程的结束逻辑
        # 主进程的代码结束
        # 所有的子进程结束
        # 给子进程回收资源
        # 主进程结束

# 主进程怎么知道子进程结束了的呢？
    # 基于网络、文件

# join方法 ：阻塞，直到子进程结束就结束
# import time
# from multiprocessing import Process
# def send_mail():
#     time.sleep(3)
#     print('发送了一封邮件')
# if __name__ == '__main__':
#     p = Process(target=send_mail)
#     p.start()   # 异步 非阻塞
#     # time.sleep(5)
#     print('join start')
#     p.join()    # 同步 阻塞 直到p对应的进程结束之后才结束阻塞
#     print('5000封邮件已发送完毕')


# 开启10个进程，给公司的5000个人发邮件，发送完邮件之后，打印一个消息“5000封邮件已发送完毕”
# import time
# import random
# from multiprocessing import Process
# def send_mail(a):
#     time.sleep(random.random())
#     print('发送了一封邮件',a)
#
# if __name__ == '__main__':
#     l = []
#     for i in range(10):
#         p = Process(target=send_mail,args=(i,))
#         p.start()
#         l.append(p)
#     print(l)
#     for p in l:p.join()
#     # 阻塞 直到上面的十个进程都结束
#     print('5000封邮件已发送完毕')

# 总结
# 1.开启一个进程
    # 函数名(参数1,参数2)
    # from multiprocessing import Process
    # p = Process(target=函数名,args=(参数1,参数2))
    # p.start()
# 2.父进程  和 子进程
# 3.父进程会等待着所有的子进程结束之后才结束
    # 为了回收资源
# 4.进程开启的过程中windows和 linux/ios之间的区别
    # 开启进程的过程需要放在if __name__ == '__main__'下
        # windows中 相当于在子进程中把主进程文件又从头到尾执行了一遍
            # 除了放在if __name__ == '__main__'下的代码
        # linux中 不执行代码,直接执行调用的func函数
# 5.join方法
    # 把一个进程的结束事件封装成一个join方法
    # 执行join方法的效果就是 阻塞直到这个子进程执行结束就结束阻塞

    # 在多个子进程中使用join
    # p_l= []
    # for i in range(10):
        # p = Process(target=函数名,args=(参数1,参数2))
        # p.start()
        # p_l.append(p)
    # for p in p_l:p.join()
    # 所有的子进程都结束之后要执行的代码写在这里















