#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
def goods_list():
    """
    商品列表
    :return:
    """
    # 读取文件中的数据，然后进行展示即可。
    print(1,'电脑',100)
    print(1,'电脑',100)
    print(1,'电脑',100)
    print(1,'电脑',100)
    print(1,'电脑',100)
    print(1,'电脑',100)

def search_goods():
    """
    模糊搜索
    :return:
    """
    while True:
        key = input('请输入要查询的关键字(N/n)：')
        if key.upper() == 'N':
            return

def create_goods():
    """
    创建商品
    :return:
    """

def user():
    """
    用户管理
    :return:
    """
    print('正在开发中...')

def goods():
    """
    商品管理
    :return:
    """
    func_dict = {'1':goods_list,'2':search_goods,'3':create_goods}
    while True:
        print('1.商品列表; 2.模糊搜索;3.录入信息')
        num = input('请选择序号(N/n):')
        if num.upper() == 'N':
            # sys.exit(0)
            return
        func = func_dict.get(num)
        if not func:
            print('输入错误，请重新输入！')
            continue
        func()

def run():
    """
    程序执行的入口
    :return:
    """
    func_dict = {'1':goods,'2':user}
    while True:
        print('1.商品管理；2.会员管理;')
        num = input('请选择序号（N/n）:')
        if num.upper() == "N":
            return
        func = func_dict.get(num) # 1 2
        # 1.简单业务先处理（简单代码往前放）
        # 2.尽量减少代码层级
        if not func:
            print('序号输入错误，请重新输入！')
            continue
        func()

run()