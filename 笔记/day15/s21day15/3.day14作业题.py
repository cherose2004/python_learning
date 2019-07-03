#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 4.
"""
写一个脚本，接收两个参数。
第一个参数：文件
第二个参数：内容
请将第二个参数中的内容写入到 文件（第一个参数）中。
"""
"""
import sys

if len(sys.argv) < 3:
    print('参数不够，请重新运行')
    # sys.exit(0)
else:
    file_path = sys.argv[1]
    content = sys.argv[2]
    with open(file_path,mode='w',encoding='utf-8') as f:
        f.write(content)
"""

# 7. 写函数实现，查看一个路径下所有的文件【所有】。
# def get_file_list(path):
#     """
#     查看路径下所有的文件
#     :param path: 指定的路径
#     :return:
#     """
#     pass

import time

# 9.1 斐波那契 4000000 内最大的数 # 0 1 1 2 3 5 ...
# num1 = 0
# num2 = 1
# count = 0
# while num2 < 4000000:
#     # print(num2) # 3524578
#     num1,num2 = num2,num1 + num2
#     count += 1
# print(num1,count)

# 9.2
"""
dic1 = {'k1':1,'k2':'alex','k3':9}
dic2 = {'k1':3,'k4':'alex','k2':'xx'}
for k,v in dic2.items():
    if k not in dic1:
        dic1[k] = v
        continue
    dic1[k] = dic1[k] + v
print(dic1)
"""


# 11.2
"""
tupleA = (11,22,33)
tupleB = ('k1','vv','asdf')
info = {}
for i in range(0,len(tupleA)):
    info[tupleA[i]] = tupleB[i]
print(info)
"""
"""
py2:
    xrange，不会在内存中立即创建，而是在循环时。边循环边创建。
    range ,在内存立即把所有的值都创建。
py3:
    range ，不会在内存中立即创建，而是在循环时。边循环边创建。
    list(range(10))
"""

# 11.7
# v = [11,22,11,22,123,123,9,1]
# v = list(set(v))
# print(v)

# 11.编程.4
# alist = [12,3,4,5]
# blist = [11,9,4,20]
# 题意一：谁大的次数多，就返回谁。
# 题意二：比较每个元素，如果a中每个元素都比b中的每个元素大，则返回a；否则返回b ；如果所有都相等则返回A；有大有小返回b
"""
需求：
    1. 按照索引依次比较两个列表中的元素。
    2. 如果A中的每个元素都比B中每个元素大（按照索引一一对应）, 则返回A列表。
    3. 如果A中的每个元素都比B中的每个元素小（按照索引一一对应），则返回B列表。
    4. A中和B中的所有都相等，则返回A
    5. A中和B中的有大有小，则返回B
"""
# result = set()
# for i in range(len(alist)):
#     if alist[i] > blist[i]:
#         result.add('a>b')
#     elif alist[i] < blist[i]:
#         result.add('a<b')
#     else:
#         result.add('a==b')
#
# if len(result) != 1:
#     print(blist)
# else:
#     ele = result.pop()
#     if ele == 'a>b' or ele == 'a==b':
#         print(alist)
#     else:
#         print(blist)


# 11.编程2
# for i in range(1,1001):
#     num_list = []
#     # 每次循环进来：都要对这个数进行求所有约数。
#     for j in range(1,i):
#         if i % j == 0:
#             num_list.append(j)
#     val = 1
#     for item in num_list:
#         val *= item
#     if i == sum(num_list) and i == val:
#         print(i)
