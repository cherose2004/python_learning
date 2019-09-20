#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from functools import reduce
def exp_format(exp):
    exp = exp.replace('--','+')
    exp = exp.replace('+-','-')
    exp = exp.replace('++','+')
    exp = exp.replace('-+','-')
    return exp

def mul_div(atom_exp):   # 最基础的两个数的加减乘除
    if '*' in atom_exp:
        a, b = atom_exp.split('*')
        res = float(a) * float(b)
    else:
        a, b = atom_exp.split('/')
        res = float(a) / float(b)
    return res

def cal_muldiv(exp):    # 匹配乘除法 计算
    com = re.compile('\d+(\.\d+)?[*/]-?\d+(\.\d+)?')
    while True:
        obj = com.search(exp)
        if obj:
            atom_exp = obj.group()
            res = mul_div(atom_exp)      # 计算a*b   a/b
            exp = exp.replace(atom_exp,str(res))
        else:break
    return exp    # 只有加减法的表达式

def cal_addsub(exp):   # 计算加减法
    ret = re.findall('[-+]?\d+(?:\.\d+)?',exp)
    count = reduce(lambda x,y:float(x)+float(y),ret)
    return count

def cal(no_bracket_exp):   # 负责完成最基本的加减乘除四则运算
    sub_exp = cal_muldiv(no_bracket_exp)  # 加减表达式 = cal_muldiv(加减乘除表达式)  做乘除法
    sub_exp = exp_format(sub_exp)  # 符号整理
    ret = cal_addsub(sub_exp)  # 计算加减法
    return ret

def remove_backet(exp):    # 去括号
    while True:
        ret = re.search('\([^()]+\)', exp)
        if ret:
            no_bracket_exp = ret.group()
            ret = cal(no_bracket_exp)
            exp = exp.replace(no_bracket_exp, str(ret))
        else:return exp

def main(exp):
    exp = exp.replace(' ','')   # 算式的去空格
    exp = remove_backet(exp)    # 去括号 并计算加减乘除
    return cal(exp)              # 最终计算一个去掉了所有括号的加减乘除的表达式

exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
ret = main(exp)
print(ret)



# 基础数据类型的增删改查
# 循环 判断
# 函数 ： 定义 调用 参数 返回值
# 类的定义 实例化 调用方法 属性

# 逻辑
    # 靠作业
    # 计算器
    # 选课系统
    # 。。。。

# 进阶的知识点
    # 网络编程
    # 并发编程
