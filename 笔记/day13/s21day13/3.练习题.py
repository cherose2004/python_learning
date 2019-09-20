#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
func_list = []
for i in range(10):
    func_list.append(lambda x:x+i)

# i=9 / func_list = [函数,函数]
for j in range(0,len(func_list)):
    # j =  0 1 2 ..9
    result = func_list[j](j) # 0 + 9 /  1 + 9
    print(result)
"""

"""
func_list = []
for i in range(10):
    func_list.append(lambda x:x+i)

# i=9 / func_list = [函数,函数,函数,函数,函数,函数,函数,函数,函数,函数]
for i in range(0,len(func_list)):
    # i=0 ; 函数(0)
    # i=1 ; 函数(1)
    # i=2 ; 函数(2)
    result = func_list[i](i)
    print(result)
"""
"""
def f1():
    print('f1')
    v = f3()
    return v

def f2():
    print('f2')
    return f1

def f3():
    print('f3')
    return 666

func = f2() # f2
result = func() # f1  f3
print(result) # 666
"""

"""
name = '景女神'
def func():
    def inner():
        print(name)
    return inner
v = func()
print(v)
"""

def func(name):
    return lambda x:x+name

v1 = func(1) # {name=1,lambda x:x+name}
v2 = func(2) # {name=2,lambda x:x+name}
result1 = v1(10)
result2 = v2(10)
print(result1,result2)