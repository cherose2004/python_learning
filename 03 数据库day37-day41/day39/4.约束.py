#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 约束
    # unsigned  设置某一个数字无符号
    # not null 某一个字段不能为空
    # default 给某个字段设置默认值
    # unique  设置某一个字段不能重复
        # 联合唯一
    # auto_increment 设置某一个int类型的字段 自动增加
        # auto_increment自带not null效果
        # 设置条件 int  unique
    # primary key    设置某一个字段非空且不能重复
        # 约束力相当于 not null + unique
        # 一张表只能由一个主键
    # foreign key    外键
        # references
        # 级联删除和更新

# not null
# default
# create table t2(
#   id int not null,
#   name char(12) not null,
#   age int default 18,
#   gender enum('male','female') not null default 'male'
# )

# unique 设置某一个字段不能重复
# create table t3(
#     id int unique,
#     username char(12) unique,
#     password char(18)
# );

# 联合唯一
# create table t4(
#     id int,
#     ip char(15),
#     server char(10),
#     port int,
#     unique(ip,port)
# );

# 自增
    # auto_increment
    # 自增字段 必须是数字 且 必须是唯一的
# create table t5(
#     id int unique auto_increment,
#     username char(10),
#     password char(18)
# )
# insert into t5(username,password) values('alex','alex3714')

# primary key  主键
    # 一张表只能设置一个主键
    # 一张表最好设置一个主键
    # 约束这个字段 非空（not null） 且 唯一（unique）

# create table t6(
#     id int not null unique,     # 你指定的第一个非空且唯一的字段会被定义成主键
#     name char(12) not null unique
# )

# create table t7(
#     id int primary key,     # 你指定的第一个非空且唯一的字段会被定义成主键
#     name char(12) not null unique
# )

# 联合主键
# create table t4(
#     id int,
#     ip char(15),
#     server char(10),
#     port int,
#     primary key(ip,port)
# );

# 外键 foreign key 涉及到两张表
# 员工表
# create table staff(
# id  int primary key auto_increment,
# age int,
# gender  enum('male','female'),
# salary  float(8,2),
# hire_date date,
# post_id int,
# foreign key(post_id) references post(pid)
# )


# 部门表
#  pid postname post_comment post_phone
# create table post(
#     pid  int  primary key,
#     postname  char(10) not null unique,
#     comment   varchar(255),
#     phone_num  char(11)
# )

# update post set pid=2 where pid = 1;
# delete from post where pid = 1;

# 级联删除和级联更新
# create table staff2(
# id  int primary key auto_increment,
# age int,
# gender  enum('male','female'),
# salary  float(8,2),
# hire_date date,
# post_id int,
# foreign key(post_id) references post(pid) on update cascade on delete set null
# )
