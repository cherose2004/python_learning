#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 创建项目之前
# 项目开发、运行过程中

# alter table 表名 add 添加字段
# alter table 表名 drop 删除字段
# alter table 表名 modify 修改已经存在的字段  的类型 宽度 约束
# alter table 表名 change 修改已经存在的字段  的类型 宽度 约束 和 字段名字

# alter table 表名 add 字段名 数据类型(宽度) 约束 first/after name
# alter table 表名 drop 字段名
# alter table 表名 modify name varchar(12) not null
# alter table 表名 change name new_name varchar(12) not null

# id name age
# alter table 表名 modify age int not null after id;
# alter table 表名 modify age int not null first;
