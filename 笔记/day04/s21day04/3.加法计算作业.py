#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
实现一个整数加法计算器(两个数相加)：

如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9（含空白），然后进行分割转换最终进行整数的计算得到结果。
"""



# 思路一：
"""
content = input('请输入：') # [5+9]  或 [5 +9]  或者 [ 5 + 9 ]
content = content.strip() # [5+9]  或 [5 +9]  或者 [5 + 9]
v1 = int(content[0])
v2 = int(content[-1])
v3 = v1 + v2 
"""

# 思路二：
"""
content = input('请输入：') # [5+9]  或 [5 +9]  或者 [ 5 + 9 ]
content_len = len(content)
index = 0
total = 0
while True:
    char = content[index]
    if char.isdigit():
        total += int(char)
    index += 1
    if index == content_len:
        break
print(total)
"""

# 思路三：
"""
content = input('请输入：') # [5+9]  或 [5 +9]  或者 [ 5 + 9 ]
result = content.split('+')
# print(result) # ['55 ', ' 99 ']
v1 = int(result[0]) # "55"
v2 = int(result[1]) # " 99 "
v3 = v1 + v2
print(v3)
"""

