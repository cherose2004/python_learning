#!/usr/bin/env python
# -*- coding:utf-8 -*-

# book ：id name price author_id
# author:aid name birthday gender

# 作者与书 一对多
# create table author(
# aid primary key auto_increment,
# name char(12) not null,
# birthday date,
# gender enum('male','female') default 'male'
# )

# create table book(
# id  int  primary key,
# name char(12) not null,
# price float(5,2)
# author_id int,
# foreign key(author_id) references author(aid)
# )

# 作者与书一对一
# create table author(
# aid primary key auto_increment,
# name char(12) not null,
# birthday date,
# gender enum('male','female') default 'male'
# )

# create table book(
# id  int  primary key,
# name char(12) not null,
# price float(5,2)
# author_id int unique,
# foreign key(author_id) references author(aid)
# )

# 作者与书多对多
# create table author(
# aid primary key auto_increment,
# name char(12) not null,
# birthday date,
# gender enum('male','female') default 'male'
# )

# create table book(
# id  int  primary key,
# name char(12) not null,
# price float(5,2)
# )

# create table book_author(
# id int primary key auto_increment,
# book_id int not null,
# author_id int not null,
# foreign key(book_id) references book(id),
# foreign key(author_id) references author(aid),
# );






