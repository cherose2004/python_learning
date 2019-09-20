#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 以email为条件查询
    # 不添加索引的时候肯定慢
    # 查询的字段不是索引字段，也慢
# id作为条件的时候
    # 如果不加索引，速度慢
    # 加了索引，速度快

# 索引不生效的原因
    # 要查询的数据的范围大
        # > < >= <= !=
        # between and
            # select * from 表 order by age limit 0，5
            # select * from 表 where id between 1000000 and 1000005;
        # like
            # 结果的范围大 索引不生效
            # 如果 abc% 索引生效，%abc索引就不生效
    # 如果一列内容的区分度不高，索引也不生效
        # name列
    # 索引列不能在条件中参与计算
        # select * from s1 where id*10 = 1000000;  索引不生效
    # 对两列内容进行条件查询
        # and and条件两端的内容，优先选择一个有索引的，并且树形结构更好的，来进行查询
            # 两个条件都成立才能完成where条件，先完成范围小的缩小后面条件的压力
            # select * from s1 where id =1000000 and email = 'eva1000000@oldboy';
        # or or条件的，不会进行优化，只是根据条件从左到右依次筛选
            # 条件中带有or的要想命中索引，这些条件中所有的列都是索引列
            # select * from s1 where id =1000000 or email = 'eva1000000@oldboy';
    # 联合索引  # create index ind_mix on s1(id,name,email);
        # select * from s1 where id =1000000 and email = 'eva1000000@oldboy';
        # 在联合索引中如果使用了or条件索引就不能生效
            # select * from s1 where id =1000000 or email = 'eva1000000@oldboy';
        # 最左前缀原则 ：在联合索引中，条件必须含有在创建索引的时候的第一个索引列
            # select * from s1 where id =1000000;    能命中索引
            # select * from s1 where email = 'eva1000000@oldboy';  不能命中索引
            # (a,b,c,d)
                # a,b
                # a,c
                # a
                # a,d
                # a,b,d
                # a,c,d
                # a,b,c,d
        # 在整个条件中，从开始出现模糊匹配的那一刻，索引就失效了
            # select * from s1 where id >1000000 and email = 'eva1000001@oldboy';
            # select * from s1 where id =1000000 and email like 'eva%';

# 什么时候用联合索引
    # 只对 a 对abc 条件进行索引
    # 而不会对b，对c进行单列的索引

# 单列索引
    # 选择一个区分度高的列建立索引，条件中的列不要参与计算，条件的范围尽量小，使用and作为条件的连接符
# 使用or来连接多个条件
    # 在满上上述条件的基础上
    # 对or相关的所有列分别创建索引

# 覆盖索引
    # 如果我们使用索引作为条件查询，查询完毕之后，不需要回表查，覆盖索引
    # explain select id from s1 where id = 1000000;
    # explain select count(id) from s1 where id > 1000000;
# 合并索引
    # 对两个字段分别创建索引，由于sql的条件让两个索引同时生效了，那么这个时候这两个索引就成为了合并索引
# 执行计划 : 如果你想在执行sql之前就知道sql语句的执行情况，那么可以使用执行计划
    # 情况1：
        # 30000000条数据
            # sql 20s
            # explain sql   --> 并不会真正的执行sql，而是会给你列出一个执行计划
    # 情况2：
        # 20条数据 --> 30000000
            # explain sql

# 原理和概念
    # b树
    # b+树
    # 聚集索引 - innodb
    # 辅助索引 - innodb myisam
# SQL索引的创建（单个、联合）、删除
# 索引的命中：范围，条件的字段是否参与计算(不能用函数)，列的区分度(长度)，条件and/or，联合索引的最左前缀问题
# 一些名词
    # 覆盖索引
    # 合并索引
# explain执行计划
# 建表、使用sql语句的时候注意的
    # char 代替 varchar
    # 连表 代替 子查询
    # 创建表的时候 固定长度的字段放在前面




