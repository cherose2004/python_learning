#!/usr/bin/env python
# -*- coding:utf-8 -*-




# 单例模式   设计模式
    # 什么是单例模式
    # 单例的应用场景
    # __new__方法 ：创建实例的  并且在init之前工作
# logging模块
    # 记录日志的
    # 用户 ：
    # 程序员 ：
        # 统计用的
        # 用来做故障排除的 debug
        # 用来记录错误，完成代码的优化的
    # logging.basicconfig
        # 使用方便
        # 不能实现 编码问题；不能同时向文件和屏幕上输出
        # logging.debug,logging.warning
    # logger对象
        # 复杂
            # 创建一个logger对象
            # 创建一个文件操作符
            # 创建一个屏幕操作符
            # 创建一个格式

            # 给logger对象绑定 文件操作符
            # 给logger对象绑定 屏幕操作符
            # 给文件操作符 设定格式
            # 给屏幕操作符 设定格式

            # 用logger对象来操作
# import logging
#
# logger = logging.getLogger()
# fh = logging.FileHandler('log.log')
# sh = logging.StreamHandler()
# logger.addHandler(fh)
# logger.addHandler(sh)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# sh.setFormatter(formatter)
# logger.warning('message')

# collections模块
    # OrderedDict
# from collections import OrderedDict
# odic = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(odic)
# for k in odic:
#     print(k,odic[k])

    # defaultdict
    # deque
    # namedtuple
# from collections import namedtuple   # 可命名元组
# Course = namedtuple('Course',['name','price','teacher'])
# python = Course('python',19800,'alex')
# print(python)
# print(python.name)
# print(python.price)
    # 创建一个类，这个类没有方法，所有属性的值都不能修改
# 什么是模块，什么是包
    # 什么是模块
        # py文件 写好了的 对程序员直接提供某方面功能的文件
        # import
        # from import 名字

    # 什么是包
        # 文件夹 存储了多个py文件的文件夹
        # 如果导入的是一个包，这个包里的模块默认是不能用的
        # 导入一个包相当于执行 __init__.py文件中的内容

# 项目名
    # bin  start
        # import os
        # import sys
        # base_path = os.path.dirname(os.path.dirname(__file__))
        # sys.path.append(base_path)

        # from src import core
    # conf 配置 settings
    # src  业务逻辑
        # student.py
            # from src import core
        # core.py
            # from conf import settings
    # db   数据文件
    # lib  扩展模块
    # log  日志文件

# 补充
    # 栈 Stack
        #后进先出是栈  lifo
    # 队列 Queue
        # 先进先出是队列 fifo

# 反射
    # hasattr
    # getattr
ab = 'test'

# import demo
# print(getattr(demo,'a'))
# print(getattr(demo,'a'))

import demo
import sys
# print(demo)
# print(sys.modules)
# print(demo is sys.modules['demo'])
# print(getattr(sys.modules['demo'],'a'))
print(getattr(sys.modules[__name__],'ab'))
# '__main__': <module '__main__' from 'D:/code/day24/1.内容回顾.py'>
    # setattr
    # delattr

# 反射
    # 通过 对象 来获取 实例变量、绑定方法
    # 通过 类   来获取  类变量、类方法、静态方法
    # 通过 模块名 来获取 模块中的任意变量（普通变量 函数  类）
    # 通过 本文件 来获取 本文件中的任意变量
        # getattr(sys.modules[__name__],'变量名')

# Foo抽象类/接口类
    # 就是给字类一个规范，让子类必须按照抽象类的规范来实现方法

# class Foo:
#     def func(self):
#         raise NotImplementedError
#
# class Son(Foo):
#     def func(self):
#         pass
#
# s = Son()
# s.func()