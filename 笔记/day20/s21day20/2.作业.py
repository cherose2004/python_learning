#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象(name=alex,pwd=123)，user对象(name=eric,pwd=666)，user对象(old,333)]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        username = input('请输入用户名：')
        password = input('请输入密码：')
        flag = False
        for row in self.user_list:
            # row是一个User对象
            if row.name == username and row.pwd == password:
                flag = True
                break
        if flag:
            print('登陆成功')
        else:
            print('用户名或密码错误')

    def register(self):
        """
        用户注册，每注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        while True:
            user = input('请输入用户名(N推出)：')
            if user.upper() == 'N':
                return
            pwd = input('请输入密码：')
            user_object = User(user,pwd)
            self.user_list.append(user_object)

    def run(self):
        """
        主程序
        :return:
        """
        print('1.注册；2.登陆')
        while True:
            choice = input('请选择：')
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            else:
                print('选择错误')


if __name__ == '__main__':
    # 开辟一块内存给obj，内存中存储 user_list = []
    obj = Account()
    obj.run()