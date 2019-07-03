#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1.获取文件夹的大小
# import os
# def dir_size(path):
#     ret = os.walk(path)
#     sum_size = 0
#     for base_path,dir_lst,file_lst in ret:
#         for file_name in file_lst:
#             size = os.path.getsize(os.path.join(base_path,file_name))
#             sum_size += size
#     return sum_size
# ret = dir_size(r'‪D:\视频\全栈 21期\day23')
# print(ret)
# os.path.abspath()   # 不可能能帮你确认一个文件的绝对路径

# 2.校验两个大文件的一致性
# import hashlib
# path1 = r'D:\视频\全栈21期\day14\05 python fullstack s21day14 回顾和补充：作业题讲解.mp4'
# path2 = r'D:\视频\全栈21期\day14\back.mp4'
# import os
#
# def file_md5(path):
#     size = os.path.getsize(path)
#     md5 = hashlib.md5()
#     with open(path,mode='rb') as f:
#         while size>1024:
#             content = f.read(1024)
#             md5.update(content)
#             size -=1024
#         else:
#             content = f.read(size)
#             md5.update(content)
#             size = 0
#     return md5.hexdigest()

# print(file_md5(path1)== file_md5(path2))



# with open(path1,mode='rb') as f:   # 10245
#     while size > 0:
#         content = f.read(1024)
#         md5.update(content)
#         size -= 1024

# 3.发红包
# import random
# def red_pack(money,num):
#     ret = random.sample(range(1,money*100),num-1)
#     ret.sort()
#     ret.insert(0,0)
#     ret.append(money*100)
#     for i in range(len(ret)-1):
#         yield (ret[i+1] - ret[i])/100
#
# ret = red_pack(200,5)
# for i in ret:
#     print(i)

# mro + super
# class A:
#     def func(self):
#         print('in a')
#
# class B(A):
#     def func(self):
#         print('in b')
#         super().func()  # 不是查找父类，而是根据mro顺序，找到自己对应的下一个类
#
# class C(A):
#     def func(self):
#         print('in c')
#         super().func()
#
# class D(B,C):
#     def func(self):
#         print('in d')
#         super().func()
#
# B().func()
# print(B.mro())












