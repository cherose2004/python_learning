#!/usr/bin/env python
# -*- coding:utf-8 -*-

# having 条件  # 过滤 组

# 部门人数大于3的部门
# select post from employee group by post having count(*) > 3

# 1.执行顺序 总是先执行where 再执行group by分组
#   所以相关先分组 之后再根据分组做某些条件筛选的时候 where都用不上
# 2.只能用having来完成

# 平均薪资大于10000的部门
# select post from employee group by post having avg(salary) > 10000


# select * from employee having age>18

# order by
    # order by 某一个字段 asc;  默认是升序asc 从小到大
    # order by 某一个字段 desc;  指定降序排列desc 从大到小
    # order by 第一个字段 asc,第二个字段 desc;
        # 指定先根据第一个字段升序排列，在第一个字段相同的情况下，再根据第二个字段排列

# limit
    # 取前n个  limit n   ==  limit 0,n
        # 考试成绩的前三名
        # 入职时间最晚的前三个
    # 分页    limit m,n   从m+1开始取n个
    # 员工展示的网页
        # 18个员工
        # 每一页展示5个员工
    # limit n offset m == limit m,n  从m+1开始取n个
