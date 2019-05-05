#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ######################### 基本定义函数 #######################
"""
def get_list_first_data():
    v = [11,22,33,44]
    print(v[0])

get_list_first_data()
"""

# ######################### 参数 #######################

def get_list_first_data(aaa): # aaa叫形式参数(形参)
    v = [11,22,33,44]
    print(v[aaa])


get_list_first_data(1) # 2/2/1调用函数时传递叫：实际参数（实参）
get_list_first_data(2)
get_list_first_data(3)
get_list_first_data(0)



