#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from datetime import datetime


def is_frozen(user):
    """
    判断用户是否已经被冻结
    :param user: 要检查的用户名
    :return:
    """
    with open('frozen.txt', 'r', encoding='utf-8') as f:
        user_list = f.readlines()
    frozen_user_list = {item.strip() for item in user_list if item.strip()}
    if user in frozen_user_list:
        return True
    return False


def register():
    """
    用户注册
    :return:
    """
    print('注册页面')
    while True:
        user = input('请输入用户(N推出)：')
        if user.upper() == 'N':
            return
        pwd = input('请输入密码：')
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('db.txt', mode='a', encoding='utf-8') as f:
            line = "%s|%s|%s\n" % (user, pwd, create_time,)
            f.write(line)


def login():
    """
    用户登陆
    :return:
    """
    print('用户登陆')
    count = 0
    while True:
        user = input('请输入用户名：')
        pwd = input('请输入密码：')

        # 判断用户名是否已经被冻结
        result = is_frozen(user)
        if result:
            print('用户名已经冻结')
            continue

        # 用户未被冻结,去db中查找用户名密码是否正确
        flag = False
        username_exists = False
        with open('db.txt', mode='r', encoding='utf-8') as f:
            for line in f:
                username, password, ctime = line.split('|')

                if username == user:
                    username_exists = True
                if username == user and password == pwd:
                    flag = True
                    print('登陆成功')
                    sys.exit(0)

        if not username_exists:
            print('用户名不存在，请重新登陆！')
            continue

        if not flag:
            print('用户或密码错误')
            if count == 2:
                print('错误次数已经达到3次')
                with open('frozen.txt', 'a', encoding='utf-8') as f:
                    f.write(user + '\n')
                return
            count += 1


def run():
    """
    程序入口
    :return:
    """
    func_dict = {'1': register, '2': login}
    while True:
        print('1.用户注册；2.用户登陆')
        choice = input('请选择：')
        func_name = func_dict.get(choice)
        if not func_name:
            print('选择错误，请重新选择！')
            continue
        func_name()


if __name__ == '__main__':
    run()
