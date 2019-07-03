#!/usr/bin/env python
# -*- coding:utf-8 -*-

# mysqldump -uroot -p123  day40 > D:\code\s21day41\day40.sql
# mysqldump -uroot -p123 --databases new_db > D:\code\s21day41\db.sql


# begin;  # 开启事务
# select * from emp where id = 1 for update;  # 查询id值，for update添加行锁；
# update emp set salary=10000 where id = 1; # 完成更新
# commit; # 提交事务










