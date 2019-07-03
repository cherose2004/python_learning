#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 数据库
    # 关系型数据库 ：mysql oracle sqlserver sqllite
    # 非关系型数据库 ：mongodb redis
# sql ：
    # ddl 定义语言
        # 创建用户
            # create user '用户名'@'%'  表示网络可以通讯的所有ip地址都可以使用这个用户名
            # create user '用户名'@'192.168.12.%' 表示192.168.12.0网段的用户可以使用这个用户名
            # create user '用户名'@'192.168.12.87' 表示只有一个ip地址可以使用这个用户名
        # 创建库
            # create database day38;
        # 创建表
            # create table 表名(字段名 数据类型(长度)，字段名 数据类型(长度)，)
    # dml 操作语言
            # 数据的
            # 增 insert into
            # 删 delete from
            # 改 update
            # 查 select
                # select user(); 查看当前用户
                # select database(); 查看当前所在的数据库
            # show
                # show databases:  查看当前的数据库有哪些
                # show tables；查看当前的库中有哪些表
            # desc 表名；查看表结构
            # use 库名；切换到这个库下
    # dcl 控制语言
        # 给用户授权
        # grant select on 库名.* to '用户名'@'ip地址/段' identified by '密码'
        # grant select,insert
        # grant all





