#!/usr/bin/env python
# -*- coding:utf-8 -*-

func_list = []
for i in range(10):
    # func_list.append(lambda :x) # 函数不被调用，内部永远不执行（不知道是什么。）
    func_list.append(lambda :i) # 函数不被调用，内部永远不执行（不知道是什么。）

print(func_list)

func_list[2]()