#!/usr/bin/env python
# -*- coding:utf-8 -*-
# create table userinfo(
# id int primary key auto_increment,
# name char(12) unique not null,
# password char(18) not null
# )
#
# insert into userinfo(name,password) values('alex','alex3714')

# 输入用户
# 输入密码
#
# 用户名和密码到数据库里查询数据
# 如果能查到数据 说明用户名和密码正确
# 如果查不到，说明用户名和密码不对
# username = input('user >>>')
# password = input('passwd >>>')
# sql = "select * from userinfo where name = '%s' and password = '%s'"%(username,password)
# print(sql)
# -- 注释掉--之后的sql语句
# select * from userinfo where name = 'alex' ;-- and password = '792164987034';
# select * from userinfo where name = 219879 or 1=1 ;-- and password = 792164987034;
# select * from userinfo where name = '219879' or 1=1 ;-- and password = '792164987034';

import pymysql

conn = pymysql.connect(host = '127.0.0.1',user = 'root',
                       password = '123',database='day41')
cur = conn.cursor()
username = input('user >>>')
password = input('passwd >>>')
sql = "select * from userinfo where name = %s and password = %s"
cur.execute(sql,(username,password))
print(cur.fetchone())
cur.close()
conn.close()