#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
# regex
# ret = re.findall('\d+','alex83')
# print(ret)
# findall 会匹配字符串中所有符合规则的项
# 并返回一个列表
# 如果未匹配到返回空列表

# ret = re.search('\d+','alex83')
# print(ret)  # 如果能匹配上返回一个对象，如果不能匹配上返回None
# if ret:
#     print(ret.group()) # 如果是对象，那么这个对象内部实现了group，所以可以取值
#                        # 如果是None，那么这个对象不可能实现了group方法，所以报错
# 会从头到尾从带匹配匹配字符串中取出第一个符合条件的项
# 如果匹配到了，返回一个对象，用group取值
# 如果没匹配到，返回None，不能用group

# re.match
# ret = re.match('\d','alex83') == re.match('^\d','alex83')
# print(ret)
# 会从头匹配字符串中取出从第一个字符开始是否符合规则
# 如果符合，就返回对象，用group取值
# 如果不符合，就返回None
# match = search + ^正则