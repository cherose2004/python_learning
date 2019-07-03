#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 单表查询
    # select (distinct)
    # from
    # where
        # 比较运算符  > < = != <> >= <=
        # 逻辑运算符 and or not
        # 身份运算符 is is not  --> null
        # 范围
            # 多选一 ：in (12,34,6) /  in ('技术','销售')
            # 数字的范围：between a and b
            # 字符串的范围
                # like   % _
                # regexp 正则
    # group by  分组
        # 聚合函数 count sum avg min max
    # having 过滤组
        # 在groupby之后执行的
        # having中可以使用聚合函数
        # having 后面的条件要么是select的字段，要么是分组的字段
    # order by
        # 排序 asc desc
    # limit  (offset)
        # limit n
        # limit m,n == limit n offset m
# 多表查询
    # 连表查询 更高效
        # 内连接 inner join
        # 外连接 left join/rignt join
    # 子查询
        # 在查询一个结果的时候，依赖一个条件也是一个sql语句
