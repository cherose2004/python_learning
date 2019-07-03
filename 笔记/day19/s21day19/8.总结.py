#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
如果写代码时，函数比较多比较乱。
1. 可以将函数归类并放到同一个类中。
2. 函数如果有一个反复使用的公共值，则可以放到对象中。
"""

class File:
    def __init__(self,path):
        self.file_path = path

    def read(self):
        print(self.file_path)

    def write(self,content):
        print(self.file_path)

    def delete(self):
        print(self.file_path)

    def update(self):
        print(self.file_path)

p1 = File('log.txt')
p1.read()

p2 = File('xxxxxx.txt')
p2.read()