#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 多表查询
    # 两张表是怎么连在一起的
    # select * from emp,department;
    # 连表查询
        # 把两张表连在一起查
        # 内链接 inner join   两张表条件不匹配的项不会出现再结果中
        # select * from emp inner join department on emp.dep_id = department.id;
        # 外连接
            # 左外连接 left join  永远显示全量的左表中的数据
            # select * from emp left join department on emp.dep_id = department.id;
            # 右外连接 right join 永远显示全量的右表中的数据
            # select * from emp right join department on emp.dep_id = department.id;
            # 全外连接
            # select * from emp left join department on emp.dep_id = department.id
            # union
            # select * from department right join emp  on emp.dep_id = department.id;
    # 子查询
        # 找技术部门的所有人的姓名
        # 先找到部门表技术部门的部门id
        # select id from department where name = '技术';
        # 再找emp表中部门id = 200
        # select name from emp where dep_id = (select id from department where name = '技术');

        # 找到技术部门和销售部门所有人的姓名
        # 先找到技术部门和销售部门的的部门id
        # select id from department where name = '技术' or name='销售'
        # 找到emp表中部门id = 200或者202的人名
        # select name from emp where dep_id in (select id from department where name = '技术' or name='销售');
        # select emp.name from emp inner join department on emp.dep_id = department.id where department.name in ('技术','销售');

# 连接的语法
# select 字段 from 表1 xxx join 表2 on 表1.字段 = 表2.字段;
    # 常用
    # 内链接
    # 左外链接

# 找技术部门的所有人的姓名
    # select * from emp inner join department on emp.dep_id = department.id;
# +----+-----------+--------+------+--------+------+--------------+
# | id | name      | sex    | age  | dep_id | id   | name         |
# +----+-----------+--------+------+--------+------+--------------+
# |  1 | egon      | male   |   18 |    200 |  200 | 技术         |
# |  2 | alex      | female |   48 |    201 |  201 | 人力资源     |
# |  3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源     |
# |  4 | yuanhao   | female |   28 |    202 |  202 | 销售         |
# |  5 | liwenzhou | male   |   18 |    200 |  200 | 技术         |
# +----+-----------+--------+------+--------+------+--------------+
# select * from emp inner join department on emp.dep_id = department.id where department.name = '技术'
# select emp.name from emp inner join department d on emp.dep_id = d.id where d.name = '技术'

# 找出年龄大于25岁的员工以及员工所在的部门名称
# select emp.name,d.name from emp inner join department as d on emp.dep_id = d.id where age>25;

# 根据age的升序顺序来连表查询emp和department
# select * from emp inner join department as d on emp.dep_id = d.id order by age;

# 优先使用连表查询，因为连表查询的效率高


# 练习
# 查询平均年龄在25岁以上的部门名
# 部门名 department表
# select name from department where id in (
#   select dep_id from emp group by dep_id having avg(age)>25
# );
# 员工表
# select dep_id,avg(age) from emp group by dep_id;
# select dep_id from emp group by dep_id having avg(age)>25;

# 查看不足1人的部门名(子查询得到的是有人的部门id)
# 查emp表中有哪些部门id
# select dep_id from emp group by dep_id;
# 再看department表中
# select * from department where id not in (???)
# select * from department where id not in (select dep_id from emp group by dep_id);

# 查询大于所有人平均年龄的员工名与年龄
# select * from emp where age>(select avg(age) from emp);

# 查询大于部门内平均年龄的员工名、年龄
# select dep_id,avg(age) from emp group by dep_id;
# select * from emp inner join (select dep_id,avg(age) avg_age from emp group by dep_id) as d
# on emp.dep_id = d.dep_id where emp.age > d.avg_age;