#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 分组 group by
# select * from employee group by post
# 会把在group by后面的这个字段，也就是post字段中的每一个不同的项都保留下来
# 并且把值是这一项的的所有行归为一组

# 聚合  把很多行的同一个字段进行一些统计，最终的到一个结果
    # count(字段) 统计这个字段有多少项
    # sum(字段)   统计这个字段对应的数值的和
    # avg(字段)   统计这个字段对应的数值的平均值
    # min(字段)
    # max(字段)

# 分组聚合
    # 求各个部门的人数
    # select count(*) from employee group by post
    # 求公司里 男生 和女生的人数
    # select count(id) from employee group by sex
    # 求各部门的平均薪资
    # 求各部门的平均年龄
    # 求各部门年龄最小的
        # select post,min(age) from employee group by post
    # 求各部门年龄最大的
    # 求各部门薪资最高的
    # 求各部门薪资最低的
    # 求最晚入职的
    # 求最早入职的
    # 求各部门最晚入职的
    # 求各部门最早入职的

# 求部门的最高薪资或者求公司的最高薪资都可以通过聚合函数取到
# 但是要得到对应的人，就必须通过多表查询

# 总是根据会重复的项来进行分组
# 分组总是和聚合函数一起用 最大 最小 平均 求和 有多少项


