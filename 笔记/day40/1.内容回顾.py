#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 约束
    # unsigned  整数类型
    # not null  非空（严格模式会影响非空设置的效果）
    # default  设置默认值
    # unique  唯一
        # 联合唯一 unique(字段1，字段2)
    # auto_increment 自增
        # 前提：必须是数字 且唯一
        # 自带：非空 自增效果
    # primary key 主键
        # 一张表只能由一个主键，并且最好有一个主键
        # 约束作用：非空且唯一
        # 联合主键：
            # primary key(字段1，字段2)
    # foreign key 外键
        # foreign key(本表字段-外键名) references 外表名(外表字段)；
        # 外键关联的那张表中的字段必须 unique
        # 级联操作：on update cascade on delete cascade

# 表与表之间的关系
    # 多对一
        # foreign key(多) references 表(一)
            # 多个学生对应一个班级
            # 多个员工对应一个部门
            # 多本书对应一个作者
            # 多个商品对应一个店铺、订单
    # 一对一
        # 后一 类型 unique
        # foreign key(后一) references 表(先一)
              # 一个客户对应一个学生 学生表有外键
              # 一个商品 有一个商品详情 详情页中有外键
    # 多对多
        # 第三张表
        # foreign key(外键名1) references 表1(主键)
        # foreign key(外键名2) references 表2(主键)
            # 多个学生对应一个班级，多个班级对应一个学生
            # 多个员工对应一个部门，多个部门对应一个员工
            # 多本书对应一个作者，多个作者对应一本书
            # 多个商品对应一个店铺、订单，多个店铺对应一个商品
            # 一个学生学习多门课程，一门课程被多个学上学习
# 数据的操作
    # 增
        # insert into 表 values (一条数据),(另一条数据);
        # insert into 表(字段1，字段2) values (值1,值2),(值1,值2);
    # 删
        # delete from 表 where 条件;
    # 改
        # update 表 set 字段=值 where 条件
    # 查
        # 单表查
            # select语句
            # select * from 表
            # select 字段 from 表
            # select 字段，字段2 from 表
            # select 字段 as 新名字 from 表
            # select 字段 新名字 from 表

            # select distince 字段 from 表； 去重
            # select 字段 *10 from 表