#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 存储引擎
    # myisam ：适合做读 插入数据比较频繁的，对修改和删除涉及少的，不支持事务、行级锁和外键。有表级锁
            #  索引和数据分开存储的，mysql5.5以下默认的存储引擎
    # innodb ：适合并发比较高的，对事务一致性要求高的，
            # 相对更适应频繁的修改和删除操作，有行级锁，外键且支持事务
            # 索引和数据是存在一起的，mysql5.6以上默认的存储引擎
    # memory ：数据存在内存中，表结构存在硬盘上，查询速度快，重启数据丢失
# 数据类型
    # 数字类型 ：int，float(5,2)
    # 字符串类型 ：char(10)，varchar(10)
    # 时间类型：datetime，date，time
    # enum和set：enum(单选项1,单选项2)，set(多选项1，多选项2)

# create table 表名(
# 字段名 数据类型(宽度/选项)，
# 字段名 数据类型(宽度/选项)，
# )

# 创建库
# create database day39
# 查看有哪些库
# show databases;
# 查看当前所在的数据库
# select database();
# 切换库
# use 库名

# database(),user(),now(),concat(),password()

# create table staff (
# id int,
# name char(12),
# gender enum('male','female'),
# hire_date date,
# salary float(8,2),
# hobby set('唱','跳','rap','打篮球'))