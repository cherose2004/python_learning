#!/usr/bin/env python
# -*- coding:utf-8 -*-

# # 二进制转化成十进制
# v1 = '0b1101'
# result = int(v1,base=2)
# print(result)
#
# # 八进制转化成十进制
# v1 = '0o1101'
# result = int(v1,base=8)
# print(result)
#
# # 十六进制转化成十进制
# v1 = '0x1101'
# result = int(v1,base=16)
# print(result)

ip = "192.168.12.79"
ip_list = ip.split('.') # ['192','168','12','79']
result = []
for item in ip_list:
    result.append(bin(int(item)))

print(''.join(result))