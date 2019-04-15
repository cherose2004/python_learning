#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

"""
def func1():
    time.sleep(2)
    print(123)

def func2():
    time.sleep(1)
    print(123)

def func3():
    time.sleep(1.5)
    print(123)


start_time1 = time.time() # 获取当前时间
func1()
end_time1 = time.time() # 获取当前时间
print(end_time1-start_time1)

start_time2 = time.time() # 获取当前时间
func2()
end_time2 = time.time() # 获取当前时间
print(end_time2-start_time2)

start_time3 = time.time() # 获取当前时间
func3()
end_time3 = time.time() # 获取当前时间
print(end_time3-start_time3)

"""

def wrapper(func):
    def inner():
        start_time = time.time()
        v = func()
        end_time = time.time()
        print(end_time-start_time)
        return v
    return inner

@wrapper
def func1():
    time.sleep(2)
    print(123)



@wrapper
def func2():
    time.sleep(1)
    print(123)

def func3():
    time.sleep(1.5)
    print(123)

func1()
