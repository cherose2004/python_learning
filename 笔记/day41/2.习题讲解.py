#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用户表 user
# create table user(
# uid int primary key auto_increment,
# username char(12)
# )

# 订单表 orders
# create table orders(
# oid  int primary key auto_increment,
# otime datetime,
# payment float(10,2),
# uid int,
# foreign key(uid) references user(uid)
# )

# insert into user(username) values ('alex'),('太白');
# insert into orders(otime,payment,uid) values (20190524093800,1320,1),(20180524093800,2000,2);

# 查订单表，按照支付时间从早到晚排序
    # 从小到大
    # select * from orders order by otime;
# 查询每个用户购买的订单数
    # select uid,count(*) from orders group by uid;   uid和订单数
    # select * from user inner join (select uid,count(*) from orders group by uid) as o on user.uid = o.uid;
    # select username,count_order from user inner join (select uid,count(*) as count_order from orders group by uid) as o on user.uid = o.uid;
# 查购买的订单总额最高的用户名
    # 查购买的订单总额最高的uid
    # select uid,sum(payment) from orders group by uid;
    # select uid,sum(payment) as sum_pay from orders group by uid order by sum_pay desc;
    # select uid,sum(payment) as sum_pay from orders group by uid order by sum_pay desc limit 1;
    # select username from user inner join (select uid,sum(payment) as sum_pay from orders group by uid order by sum_pay desc limit 1) pay on user.uid = pay.uid;

# 删除订单编号为3的订单信息
    # delete from orders where oid = 2;

# 订单4的支付金额修改成400
    # update orders set payment=400 where oid=4;











