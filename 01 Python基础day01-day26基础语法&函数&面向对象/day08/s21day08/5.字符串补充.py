#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 首字母大写
# v = 'alex'
# v1 = v.capitalize()
# print(v1)

# 牛逼的小写 casefold

# center，居中
# v = 'alex'
# v1 = v.center(20,'*')
# print(v1,len(v1))

# ljust / rjust
# v = 'alex'
# v1 = v.rjust(20,'*')
# print(v1)

# count  计算子序列出现的次数
# v = 'aealeax'
# v1 = v.count('ea')
# print(v1)

# find，找索引位置(从左到右找到第一个),存在则返回索引位置，不存在则返回 -1
# index， 找索引位置(从左到右找到第一个),存在则返回索引位置，不存报错
# v = 'alexex'
# index = v.find('u')
# print(index)


# format/format_map
# v= '我是{0},谢谢谢 {1}'.format('alex',19)
# print(v)
# v= '我是{x1},谢谢谢 {xx}'.format_map({'x1':'alex','xx':19})
# print(v)

#
# v = 'asdf3rsdfsdf32sfd'

# v1 = v.split('3')
# print(v1)
# v1 = v.partition('3') # 将指定字符串分为三分：前面，自己，后面
# print(v1)

# v = 'aleX is sb'
#
# v1 = v.title()
# print(v1)


# v = "alex"
# v1 = v.zfill(20)
# print(v1)
#
# a = '12345'
# b = 'aeiou'
# table = str.maketrans(b,a)
# v = 'adsqwoufjaadsfqwerasdfa;sjdfasfd'
# # v = '1dsqw45fj11dsfqw2r1sdf1;sjdf1sfd'
# result = v.translate(table)
# print(result)