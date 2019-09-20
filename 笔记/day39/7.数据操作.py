#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 增加 insert
# 删除 delete
# 修改 update
# 查询 select

# 增加 insert
# insert into 表名 values (值....)
    # 所有的在这个表中的字段都需要按照顺序被填写在这里
# insert into 表名(字段名，字段名。。。) values (值....)
    # 所有在字段位置填写了名字的字段和后面的值必须是一一对应
# insert into 表名(字段名，字段名。。。) values (值....),(值....),(值....)
    # 所有在字段位置填写了名字的字段和后面的值必须是一一对应

# value单数            values复数
# 一次性写入一行数据   一次性写入多行数据

# t1 id,name,age
# insert into t1 value (1,'alex',83)
# insert into t1 values (1,'alex',83),(2,'wusir',74)

# insert into t1(name,age) value ('alex',83)
# insert into t1(name,age) values ('alex',83),('wusir',74)

# 第一个角度
    # 写入一行内容还是写入多行
    # insert into 表名 values (值....)
    # insert into 表名 values (值....)，(值....)，(值....)

# 第二个角度
    # 是把这一行所有的内容都写入
    # insert into 表名 values (值....)
    # 指定字段写入
    # insert into 表名(字段1，字段2) values (值1，值2)


# 删除 delete
    # delete from 表 where 条件;

# 更新 update
    # update 表 set 字段=新的值 where 条件；

# 查询
    # select语句
        # select * from 表
        # select 字段,字段.. from 表
        # select distinct 字段,字段.. from 表  # 按照查出来的字段去重
        # select 字段*5 from 表  # 按照查出来的字段去重
        # select 字段  as 新名字,字段 as 新名字 from 表  # 按照查出来的字段去重
        # select 字段 新名字 from 表  # 按照查出来的字段去重

