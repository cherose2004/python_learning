#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 比较运算 > < = >= <= != <>
# 范围筛选
    # 多选一 字段名 in (值1,值2，值3)
        # 20000,30000,3000,19000,18000,17000
            # select * from employee where salary in (20000,30000,3000,19000,18000,17000)
    # 在一个模糊的范围里  between 10000 and 20000
        # 在一个数值区间  1w-2w之间的所有人的名字
            # select emp_name from employee where salary between 10000 and 20000;
        # 字符串的模糊查询 like
            # 通配符 % 匹配任意长度的任意内容
            # 通配符 _ 匹配一个字符长度的任意内容
        # 正则匹配 regexp  更加细粒度的匹配的时候
            # select * from 表 where 字段 regexp 正则表达式
            # select * from employee where emp_name regexp '^j[a-z]{5}'
# 逻辑运算 - 条件的拼接
    # 与 and
    # 或 or
    # 非 not
        # select * from employee where salary not in (20000,30000,3000,19000,18000,17000)

# 身份运算 - 关于null  is null /is not null
    # 查看岗位描述不为NULL的员工信息
    # select * from employee where post_comment is not null;

# 查看岗位是teacher且名字是jin开头的员工姓名、年薪
    #select emp_name,salary*12 from employee where post='teacher' and emp_name like 'jin%'
    #select emp_name,salary*12 from employee where post='teacher' and emp_name regexp '^jin.*'














