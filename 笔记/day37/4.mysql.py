#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 数据库
    # 很多功能如果只是通过操作文件来改变数据是非常繁琐的
        # 程序员需要做很多事情
    # 对于多台机器或者多个进程操作用一份数据
        # 程序员自己解决并发和安全问题比较麻烦
    # 自己处理一些数据备份，容错的措施

# C/S架构的 操作数据文件的一个管理软件
    # 1.帮助我们解决并发问题
    # 2.能够帮助我们用更简单更快速的方式完成数据的增删改查
    # 3.能够给我们提供一些容错、高可用的机制
    # 4.权限的认证

# 数据库管理系统 —— 专门用来管理数据文件，帮助用户更简洁的操作数据的软件
    # DBMS
# 数据 data
# 文件
# 文件夹 -- 数据库database db
# 数据库管理员 —— DBA

# 数据库管理系统
    # 关系型数据库
        # sql server
        # oracle 收费、比较严谨、安全性比较高
            # 国企 事业单位
            # 银行 金融行业
        # mysql  开源的
            # 小公司
            # 互联网公司
        # sqllite
    # 非关系型数据库
        # redis
        # mongodb

# 安装mysql遇到的问题
    # 操作系统的问题
        # 缺失dll文件
    # 安装路径
        # 不能有空格
        # 不能有中文
        # 不能带着有转义的特殊字符开头的文件夹名
    # 安装之后发现配置有问题
        # 再修改配置往往不能生效
    # 卸载之后重装
        # mysqld remove
        # 把所有的配置、环境变量修改到正确的样子
        # 重启计算机 - 清空注册表
        # 再重新安装

# mysql的CS架构
    # mysqld install  安装数据库服务
    # net start mysql 启动数据库的server端
        # 停止server net stop mysql
    # 客户端可以是python代码也可以是一个程序
        # mysql.exe是一个客户端
        # mysql -u用户名 -p密码
# mysql中的用户和权限
    # 在安装数据库之后，有一个最高权限的用户root
    # mysql 192.168.12.87 eva/123
        # mysql -h192.168.12.87 -uroot -p123

# 我们的mysql客户端不仅可以连接本地的数据库
# 也可以连接网络上的某一个数据库的server端

# mysql>select user();
    # 查看当前用户是谁
# mysql>set password = password('密码')
    # 设置密码
# 创建用户
# create user 's21'@'192.168.12.%' identified by '123';
# mysql -us21 -p123 -h192.168.12.87

# 授权
    # grant all on day37.* to 's21'@'192.168.12.%';
    # 授权并创建用户
    # grant all on day37.* to 'alex'@'%' identified by '123';

# 查看文件夹
    # show databases;
# 创建文件夹
    # create database day37;

# 库 表 数据
    # 创建库、创建表  DDL数据库定义语言
    # 存数据，删除数据,修改数据,查看  DML数据库操纵语句
    # grant/revoke  DCL控制权限
# 库
    # create database 数据库名;  # 创建库
    # show databases; # 查看当前有多少个数据库
    # select database();# 查看当前使用的数据库
    # use 数据库的名字; # 切换到这个数据库(文件夹)下
# 表操作
    # 查看当前文件夹中有多少张表
        # show tables;
    # 创建表
        # create table student(id int,name char(4));
    # 删除表
        # drop table student;
    # 查看表结构
        # desc 表名;

# 操作表中的数据
    # 数据的增加
        # insert into student values (1,'alex');
        # insert into student values (2,'wusir');
    # 数据的查看
        # select * from student;
    # 修改数据
        # update 表 set 字段名=值
        # update student set name = 'yuan';
        # update student set name = 'wusir' where id=2;
    # 删除数据
        # delete from 表名字;
        # delete from student where id=1;


# 把创建用户，给用户授权，登陆一下同桌的mysql server，给同桌开一个账号
# 操作库 表 数据






