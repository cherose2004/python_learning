#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 有一个文件，这个文件中有20001行数据，开启一个线程池，为每100行创建一个任务，
# 打印这100行数据。

def print_line(lines):
    print(lines)

from concurrent.futures import ThreadPoolExecutor
tp = ThreadPoolExecutor(20)
with open('file',encoding='utf-8') as f:
    lines = []
    for line in f:
        if len(lines) == 100:
            tp.submit(print_line,lines)
            lines.clear()
        lines.append(line)
    if lines:
        tp.submit(print_line, lines)

def print_line(lines):
    print(lines)   # 涉及到的io操作时间长

def read_file(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            yield line

def submit_func(tp,line=None,end= False,lines = []):
    if line:
        lines.append(line)
    if len(lines) == 100 or end:
        line_lst = lines.copy()
        tp.submit(print_line, line_lst)
        lines.clear()

from concurrent.futures import ThreadPoolExecutor

tp = ThreadPoolExecutor(20)
for line in read_file('file'):
    submit_func(tp,line)
submit_func(tp,end=True)

# python 引用语义的语言 所有的赋值、传参都是传递的值的内存地址
# c 值语义的语言 所有的赋值、传参都是传递的值本身

# 直接开个线程池
    # 每一个线程负责使用同一个文件句柄
    # 读文件

