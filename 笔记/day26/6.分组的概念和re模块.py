#!/usr/bin/env python
# -*- coding:utf-8 -*-

s1 = '<h1>wahaha</h1>'
s2 = '<a>wahaha ya wahaha</a>'
# s1 -> h1  wahaha
# s2 -> a   wahaha ya wahaha
import re

# ret = re.search('<(\w+)>(.*?)</\w+>',s1)
# print(ret)
# print(ret.group(0))   # group参数默认为0 表示取整个正则匹配的结果
# print(ret.group(1))   # 取第一个分组中的内容
# print(ret.group(2))   # 取第二个分组中的内容

# ret = re.search('<(?P<tag>\w+)>(?P<cont>.*?)</\w+>',s1)
# print(ret)
# print(ret.group('tag'))   # 取tag分组中的内容
# print(ret.group('cont'))   # 取cont分组中的内容

# 分组命名
# (?P<名字>正则表达式)
# 引用分组  (?P=组名)   这个组中的内容必须完全和之前已经存在的组匹配到的内容一模一样

# s1 = '<h1>wahaha</h1>'
# s2 = '<a>wahaha ya wahaha</a>'
# ret = re.search('<(?P<tag>\w+)>.*?</(?P=tag)>',s1)
# print(ret.group('tag'))

# s1 = '<h1>wahaha</h1>'
# s2 = '<a>wahaha ya wahaha</a>'
# ret = re.search(r'<(\w+)>.*?</\1>',s1)
# print(ret.group(1))





import re

# ret = re.findall('\d(\d)','aa1alex83')
# # findall遇到正则表达式中的分组，会优先显示分组中的内容
# print(ret)

# ret = re.findall('\d+(?:\.\d+)?','1.234+2')
# print(ret)

# 分组
# split
    # 会保留分组中本来应该被切割掉的内容
# 分组命名
# (?P<名字>正则)  search group('组名')
# 引用分组
# (?P=组命) 表示这个组中的内容必须和之前已经存在的一组匹配到的内容完全一致
# 分组和findall
    # 默认findall 优先显示分组内的内容
    # 取消分组优先显示 (?:正则)

# 例题
    # 有的时候我们想匹配的内容包含在不相匹配的内容当中，这个时候只需要把不想匹配的先匹配出来，再通过手段去掉
# import re
# ret=re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# ret.remove('')
# print(ret)