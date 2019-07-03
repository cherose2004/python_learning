#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 表的存储方式
    # 存储方式1：MyISAM 5.5以下 默认存储方式
        # 存储的文件个数：表结构、表中的数据、索引
        # 支持表级锁
        # 不支持行级锁 不支持事务 不支持外键
    # 存储方式2：InnoDB 5.6以上 默认存储方式
        # 存储的文件个数：表结构、表中的数据
        # 支持行级锁、支持表锁
        # 支持事务
        # 支持外键
    # 存储方式3： MEMORY 内存
        # 存储的文件个数：表结构
        # 优势 ：增删改查都很快
        # 劣势 ：重启数据消失、容量有限
# 索引 - 数据库的目录


# 查看配置项:
    # show variables like '%engine%';

# 创建表
# create table t1 (id int,name char(4));
# create table t2 (id int,name char(4)) engine=myisam;
# create table t3 (id int,name char(4)) engine=memory;

# 查看表的结构
    # show create table 表名; 能够看到和这张表相关的所有信息
    # desc 表名               只能查看表的字段的基础信息
        # describe 表名


# 用什么数据库 ： mysql
# 版本是什么 ：5.6
# 都用这个版本么 ：不是都用这个版本
# 存储引擎 ：innodb
# 为什么要用这个存储引擎：
    # 支持事务 支持外键 支持行级锁
                         # 能够更好的处理并发的修改问题









