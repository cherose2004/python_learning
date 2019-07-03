#!/usr/bin/env python
# -*- coding:utf-8 -*-
def creat_list1(file):
    with open("a.log",mode="r",encoding="utf-8") as file1:
        content=file1.read()
        data=content.split("\n")
        return data

def creat_list2(file):
    new_list=[]
    with open("a.log",mode="r",encoding="utf-8") as file1:
        content=file1.read()
        data=content.split("\n")
        for x in data :
            data1=x.split("|")
            new_list.append(data1)
        return new_list

def creat_list3(file):
    new_list=[]
    with open("a.log",mode="r",encoding="utf-8") as file1:
        content=file1.read()
        data=content.split("\n")
        dict1 = {}
        for x in data :
            data1=x.split("|")
            new_list.append(data1)
        val=["name","pwd","age"]
        for i in range(len(new_list)):
            dict1[val[i]]=new_list[i]
        return dict1