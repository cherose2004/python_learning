#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1. 计算长度
# value = "alex"
# number = len(value)
# print(number)

# 2. 索引
"""
value = 'alexasdfasdfasdfasdfas'
# v1 = value[4]
# print(v1)
value_len = len(value) # 4
index = 0
while True:
    val = value[index]
    print(val)
    if index == value_len-1:
        break

    index += 1

"""
# v = "oldboy"
# v1 = v[0]  # 0 1 2 3 ...
# v2 = v[-3]
# print(v2)


# 3. 切片
# v = "oldboy"
# v1 = v[2:4] #   2 =< 索引位置 <3
# v2 = v[3:6]
# v2 = v[3:-1]
# v2 = v[3:]
# v2 = v[:-1]
# print(v2)

# 示例: 取最后两个字符
# data = input('请输入：')
# 方式一
# v = data[-2:]
# print(v)
# 方式二
# total_len = len(data)
# v = data[total_len-2:total_len]
# print(v)

# 练习题1
"""
需求：让用户输入任意字符串，获取字符串之后并计算其中有多少个数字。
"""
"""
total = 0
text = input('请输入内容：') # ads2kjf5adja453421sdfsdf
index_len = len(text)
index = 0
while True:
    val = text[index]
    #print(val) # "a"
    # 判断val是否是数字
    #     - 是数字：total + 1
    #     -   不是：继续玩下走，执行下一次循环去检查下一个字符。
    flag = val.isdigit()
    if flag:
        total = total + 1 # total += 1
    if index == index_len - 1:
        break
    index += 1

print(total)
"""