#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
v1 = [11,22,33,44]

# 列表转换成迭代器
v2 = iter(v1)
result1 = v2.__next__()
print(result1)
result2 = v2.__next__()
print(result2)
result3 = v2.__next__()
print(result3)
result4 = v2.__next__()
print(result4)
result5 = v2.__next__()
print(result5)
"""
# v1 = "alex"
# v2 = iter(v1)
# while True:
#     try:
#         val = v2.__next__()
#         print(val)
#     except Exception as e:
#         break

# v1 = [11,22,33,44]
# # v2 = iter(v1)
# v2 = v1.__iter__()
# while True:
#     val = v2.__next__()
#     print(val)


# v1 = [11,22,33,44]
#
# # 1.内部会将v1转换成迭代器
# # 2.内部反复执行 迭代器.__next__()
# # 3.取完不报错
# for item in v1:
#     print(item)
# ##########################################################
v1 = [11,22,33,44]
result = v1.__iter__()