#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""
# 1. 空集合

# v = {} # 空字典
# v1 = set()
# print(type(v1))
"""
None
int
    v1 = 123
    v1 = int() --> 0
bool
    v2 = True/False
    v2 = bool() -> False
str
    v3 = ""
    v3 = str()
list
    v4 = []
    v4 = list()
tuple
    v5 = ()
    v5 = tuple()
dict
    v6 = {}
    v6 = dict()
set
    v7 = set()

"""

# 2. 独有功能

# 2.1 add添加
# v = {1,2}
# v.add('Lishaoqi')
# v.add('Lishaoqi')
# print(v)

# 2.2 删除
# v = {1,2,'李邵奇'}
# v.discard('李邵奇')
# print(v)

# 2.3 批量添加
# v = {1,2,'李邵奇'}
# v.update({11,22,33})
# print(v)

# 2.4. 交集
# v = {1,2,'李邵奇'}
# result = v.intersection({1,'李邵奇','小黑'})
# print(result)

# 2.4 并集
# v = {1,2,'李邵奇'}
# result = v.union({1,'李邵奇','小黑'})
# print(result)

# 2.5 差集
# v = {1,2,'李邵奇'}
# result = v.difference({1,'李邵奇','小黑'}) # v中有且{1,'李邵奇','小黑'}没有
# print(result)
#
# v1 = {1,'李邵奇','小黑'}
# result1 = v1.difference({1,2,'李邵奇'})
# print(result1)

# 2.6 对称差集
# v = {1,2,'李邵奇'}
# result = v.symmetric_difference({1,'李邵奇','小黑'})
# print(result)

# 注意：
# v = {1,2,'李邵奇'}
# result = v.intersection([1,'李邵奇','小黑'])
# print(result)

# ##################################################
# 3.1 len
# v = {1,2,'李邵奇'}
# print(len(v))

# 3.2 循环
# v = {1,2,'李邵奇'}
# for item in v:
#     print(item)


# ##################################################
# 1. 列表/字典/集合 -> 不能放在集合中+不能作为字典的key（unhashable）
# # info = {1, 2, 3, 4, True, "国风", None, (1, 2, 3)}
# # print(info)
# # 2. hash -> 哈希是怎么回事？
# # 因为在内部会将值进行哈希算法并得到一个数值（对应内存地址），以后用于快速查找。
#
# # 3. 特殊情况
# # info = {0, 2, 3, 4, False, "国风", None, (1, 2, 3)}
# # print(info)
#
# # info = {
# #     1:'alex',
# #     True:'oldboy'
# # }
# # print(info)

"""
v1 = [1,2,3]
v2 = v1
v1.append(999)
print(v1,v2)
print(id(v1),id(v2))
"""

"""
v1 = [1,2,3]
v2 = v1
print(id(v1),id(v2))
v1 = 999
print(id(v1),id(v2))
"""