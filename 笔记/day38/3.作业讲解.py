#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 有一个文件，这个文件中有20001行数据，开启一个线程池，为每100行创建一个任务，打印这100行数据。

# def print_line(lines):
#     print(lines)
#
# from concurrent.futures import ThreadPoolExecutor
# tp = ThreadPoolExecutor(20)
# with open('file',encoding='utf-8') as f:
#     lines = []
#     for line in f:
#         if len(lines) == 100:
#             tp.submit(print_line,lines)
#             lines.clear()
#         lines.append(line)
#     if lines:
#         tp.submit(print_line, lines)

# def print_line(lines):
#     print(lines)
#
# def read_file(filename):
#     with open(filename, encoding='utf-8') as f:
#         for line in f:
#             yield line
#
# def submit_func(tp,line=None,end= False,lines = []):
#     if line:
#         lines.append(line)
#     if len(lines) == 100 or end:
#         tp.submit(print_line, lines)
#         lines.clear()
#
# from concurrent.futures import ThreadPoolExecutor
#
# tp = ThreadPoolExecutor(20)
# for line in read_file('file'):
#     submit_func(tp,line)
# submit_func(tp,end=True)

# 1. print 和 文件的读 写 都是io操作,
    # 这个题主要就是起线程在一个线程读文件的时候，利用这个线程读取文件的时间交给另一个线程来进行打印操作
# 2. 使用线程可以有效的规避掉io操作的时间，提高程序的的效率
# 3.解耦程序的功能
# 4.默认参数是列表

