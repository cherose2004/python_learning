#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Person:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g

    def show(self):
        temp = "我是%s,年龄：%s,性别：%s " % (self.name, self.age, self.gender,)
        print(temp)

# 类() 实例化对象，自动执行此类中的 __init__方法。
p1 = Person('李兆琪',19,'男')
p1.show()

p2 = Person('利奇航',19,'男')
p2.show()

