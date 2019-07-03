#!/usr/bin/env python
# -*- coding:utf-8 -*-

# v = 55
# v1 = float(55)
# print(v1)

# v = 55.5
# v1 = int(v)
# print(v1)



# v = [1,2,311,21,3,]
# result = sum(v)
# print(result)



# a,b = divmod(1001,5)
# print(a,b)

# 请通过分页对数据进行展示
"""
要求：
    每页显示10条数据
    让用户输入要查看的页面：页码
"""

USER_LIST = []
for i in range(1,836):
    temp = {'name':'你少妻-%s' %i,'email':'123%s@qq.com' %i }
    USER_LIST.append(temp)

# 数据总条数
total_count = len(USER_LIST)

# 每页显示10条
per_page_count= 10

# 总页码数
max_page_num,a = divmod(total_count,per_page_count)
if a>0:
    max_page_num += 1

while True:
    pager = int(input('要查看第几页：'))
    if pager < 1 or pager > max_page_num:
        print('页码不合法，必须是 1 ~ %s' %max_page_num )
    else:
        """
        # 第1页：USER_LIST[0:10] -> 0123456789
        # 第2页：USER_LIST[10:20]
        # 第3页：USER_LIST[20:30]
        ...
        """
        start = (pager-1) * per_page_count
        end = pager * per_page_count
        data = USER_LIST[start:end]
        for item in data:
            print(item)







