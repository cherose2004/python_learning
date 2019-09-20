#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', user='root', password="123",
#                  database='day40')
# cur = conn.cursor()   # 数据库操作符 游标
# # cur.execute('insert into employee(emp_name,sex,age,hire_date) '
# #             'values ("郭凯丰","male",40,20190808)')
# # cur.execute('delete from employee where id = 18')
# conn.commit()
# conn.close()


# conn = pymysql.connect(host='127.0.0.1', user='root', password="123",
#                  database='day40')
# cur = conn.cursor(pymysql.cursors.DictCursor)   # 数据库操作符 游标
# cur.execute('select * from employee '
#             'where id > 10')
# ret = cur.fetchone()
# print(ret['emp_name'])
# # ret = cur.fetchmany(5)
# ret = cur.fetchall()
# print(ret)
# conn.close()

# select * from employee where id > 10


# sql注入风险