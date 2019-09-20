# -*- coding: utf-8 -*-
# __author__ = "maple"

# def func(arg):
#     print(arg)
#
# for item in range(10):
#     func(item)

"""
func_list = []

def func(arg):
    def inner():
        print(arg)
    return inner

for item in range(10):
    func_list.append(func(item))

func_list[0]()
func_list[1]()
"""

"""
func_list = []
def func():
    print(item)
for item in range(10):
    func_list.append(func)
func_list[0]()
func_list[1]()
"""