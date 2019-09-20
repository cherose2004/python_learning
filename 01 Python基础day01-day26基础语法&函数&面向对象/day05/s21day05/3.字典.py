#!/usr/bin/env python
# -*- coding:utf-8 -*-

# info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}

# info.keys() # 获取字典中的所有键  "name"   'age'  'gender'  'hobby'
# info.values() # 获取字典中的所有键  '刘伟达'  18  ''男''  ''同桌''

# for item in info.keys():
#     print(item)
#
# for item in info.values():
#     print(item)

# for v1,v2 in info.items():
#     print(v1,v2)


info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}

del info['name']
print(info)
