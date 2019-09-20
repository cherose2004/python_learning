#!/usr/bin/env python
# -*- coding:utf-8 -*-

# char(15)  定长的单位
    # alex  alex
    # alex
# varchar(15) 变长的单位
    # alex  alex4

# 哪一个存储方式好？
    # varchar ：节省空间、存取效率相对低
    # char ：浪费空间，存取效率相对高 长度变化小的

# 手机号码、身份证号  char
# 用户名、密码  char
# 评论  微博 说说 微信状态 varchar

# create table t11 (name1 char(5),name2 varchar(5));