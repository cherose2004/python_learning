#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""

# 4
"""
info = {'name':'王刚蛋','hobby':'铁锤'}
while True:
    data = input('请输入：')
    val = info.get(data,'键不存在')
    print(val)
"""

# 5
info = {'name':'王刚蛋','hobby':'铁锤','age':'18'}
# 请用代码验证 "name" 是否在字典的键中
if 'name' in info:
    print('在')

# 6
"""
info = {'name':'王刚蛋','hobby':'铁锤','age':'18'}
flag = False
for v in info.values():
    if v == "alex":
        flag = True
        break
if flag:
    print('在')
else:
    print('不在')
"""

# 7
"""
data_list = []
while True:
    value = input('请输入：') # N/n
    # if value == 'N' or value == 'n':
    #     break
    if value.upper() == 'N':
        break
    data_list.append(value)
"""

# 10
"""
v1 = {'alex','武sir','肖大'}
v2 = []
while True:
    v = input('>>>')
    if v in v1:
        v2.append(v)
    else:
        v1.add(v)
"""

# 13.
"""
v = {'k1':'v1'}
# 判断v是不是字符串？
if type(v) == str:
    print('v是字符串')
elif type(v) == dict:
    print('v是字典')
elif type(v) == list:
    print('v是列表')
elif type(v) == tuple:
    print('元组')
elif type(v) == set:
    print('集合')
"""

# ##################################### 回顾 ###########################################
"""
v1 = [1,2,3]
v2 = [1,2,3]


v1 = [1,2,3]
v2 = v1
v3 = v1
v1.append(999)


v1 = [1,2,3]
v2 = v1
v3 = v1
v1 = [1,]


v1 = [1,2,3]
v2 = v1
v3 = v1
v2 = [1,]



v1 = [1,2,3]
v2 = v1
v3 = v2

v2 = [1,]
"""
"""
v1 = "alex"
v2 = v1 
data = v1.upper()
print(v1,v2)


v1 = [11,2,3]
v2 = v1 
v1.append(999)
print(v1,v2)
"""

# v1 = "alex"
# value = v1[0:2]

"""
v1 = {1,2,3}
v2 = v1 
v1.add(666)

print(v1,v2) # 1,23,666
"""

"""
v1 = {1,2,3}
v2 = v1 
n = v1.intersection([1,88,9])
print(v1,v2) # 1,23,666
"""

"""

v1 = [1,2,3,]
v2 = v1 
v1[0] = [11,22,33,4]
"""

"""
v1 = [1,2]
v2 = [1,2,v1]
v2[2] = 55
print(v1,v2)
"""

"""
v1 = [1,2]
v2 = [1,2,v1]
v2[2][1] = 55
print(v1,v2)
"""



# #############################################################
# data = [1,2,3,4]
# nums = []
# for i in data:
#     # nums.append(i)
#     nums.append(str(i))
#
# print(id(data[0]))
# print(id(nums[0]))

#
# data = ["alex",'eric','seven']
# nums = []
# for i in data:
#     # nums.append(i.upper())
#     nums.append(i + 'xxx')
#
# print(id(data[0]))
# print(id(nums[0]))

"""
v1 = [
    [1,2,3],
    [3,4,5],
]
v2 = []
for item in v1:
    v2.append(item)
print(id(v1),id(v2))
print(id(v1[0]),id(v2[0]))
"""
