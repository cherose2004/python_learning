#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 练习1：请将user中的元素根据 _ 链接，并写入 'a1.txt' 的文件
"""
user = ['alex','eric']
data = "_".join(user)
file_object = open('a1.txt',mode='w',encoding='utf-8')
file_object.write(data)
file_object.close()
"""

# 练习2：请将user中的元素根据 _ 链接，并写入 'a1.txt' 的文件
"""
user = [
    {'name':'alex','pwd':'123'},    # alex|123
    {'name':'eric','pwd':'olbody'}, # eric|olbody
]
file_object = open('a2.txt',mode='w',encoding='utf-8')
for item in user:
    line = "%s|%s\n" %(item['name'],item['pwd'],)
    file_object.write(line)
file_object.close()
"""

# 练习3：请将a2.txt中的文件读取出来并添加到一个列表中 ['alex|123','eric|olbody']
# 方式一
"""
file_obj = open('a2.txt',mode='r',encoding='utf-8')
content = file_obj.read()
file_obj.close()
content = content.strip()
data_list = content.split('\n')
print(data_list)
"""

"""
result = []
file_obj = open('a2.txt',mode='r',encoding='utf-8')
for line in file_obj:
    line = line.strip()
    result.append(line)
file_obj.close()
print(result)
"""

