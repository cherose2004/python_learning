# -*- coding: utf-8 -*-
# __author__ = "maple"

# 1.公司有多少台服务器 有哪些业务
    #   有多少数据库平台 否则 谁来维护数据库
    #   常用的数据库版本 ： 5.6  5.7  8.0
    #   项目上线多长时间了？ 数据量  qps  表结构
    #   数据库表结构是谁设计的
    #   表关联关系 和有多少张表 对应的业务
    #   常用的sql
    #   项目所用的表中是否用到了索引 为什么要用
# 2.设计表结构
    #   建立约束和关联
    #   查询sql的角度
# 3.给你现成的表结构考sql
    # sql的查询
    # select语句不能有问题（分组聚合）单表查和多表查
# 4.考优化
    # 架构建表 ：
        # 读写分离（select语句执行效率慢）  分库分表
            # 水平分表
            # 垂直分表
        # 尽量把定长的字段放前面，尽量多使用定长字段
        # 建立索引
    # sql语句
        # 尽量在where阶段缩小范围
        # 多表查 尽量用链表代替子查询
        # 命中索引
# 5.考细节
    # char 和 varchar区别
    # 搜索的时候创建 一个 唯一索引和只创建普通index的区别

# 关系型数据库和非关系型数据库
# 存储引擎 ： innodb
            # 支持外键、事务、行级锁
# 库的操作
    # 创建库 create database 库名
    # 使用库 use 库名
    # 查看库 show databases
# 表的操作
    # 查看有哪些表 show tables
    # 创建表 ： create table 表名(字段名 类型(长度) 约束,...);
        # 数据类型： 时间 数字类型 字符串 集合枚举
        # 约束 ：unsigned,unique，not null，default,auto_incremrent,primary key,foreign key.
    # 查看表结构 :
        # desc 表名;
        # show create table 表名;
    # 修改表 :
        # alter table 表名 add 字段名 类型(长度) 约束;
        # alter table 表名 modify 字段名 类型(长度) 约束;
        # alter table 表名 drop 字段名;
        # alter table 表名 change 旧字段名 新字段名 类型(长度) 约束;
    # 删除表
        # drop table 表名
# 数据的操作
    # 增  insert into 表名(字段名) values(值)
    # 删  delete form 表名 where 条件
    # 改  update 表名 set 字段=值，字段2=值2 where 条件
    # 查  select 字段 from 表 where 条件 group by 字段 having 聚合函数 order by 列 limit n；
        # 聚合函数 ：avg sum count max min
        # 连表 ： left join ，right join ，inner join
        # 子查询：一个以上的select
# 索引
    # 创建索引 ： create index 索引名 on 表(字段名)
    # 删除索引 :  drop index 索引名 on 表
    # 命中索引
        # 1.在条件中使用了函数 四则运算
        # 2.在条件中使用了范围
        # 3.like条件%放在条件开始
        # 4.联合索引 (a,b,c,d)
            # 最左前缀原则 条件中必须有a
            # 不能用or
            # 从左到右第一个使用了范围的条件之后的所有列索引失效
        # 5.对区分度不高的列创建索引
        # 6.在条件中使用了or，并且用or相连的字段没有全部创建索引
      # 两个概念
        # 覆盖索引 ：
            # select count(age) from 表 where age>10
        # 索引合并 :
            # 分别对两个字段创建索引，但是使用的时候临时合并在一起了
            # create index ind_age on t(age)
            # create index ind_name on t(name)
            # where name='alex' or age=84
# pyymysql模块











