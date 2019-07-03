#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
from datetime import datetime

CURRENT_USER = None


def auth(func):
    def inner(*args, **kwargs):
        if not CURRENT_USER: # True
            print('用户未登陆，请登陆后在查看')
            return None
        return func(*args, **kwargs)

    return inner


@auth
def car():
    folder_path = os.path.join('shopping_car', CURRENT_USER)
    if not os.path.exists(folder_path):
        print('购物车为空')
        os.makedirs(folder_path)
        return

    for path in os.listdir(folder_path):
        print(path)
        file_path = os.path.join(folder_path, path)
        with open(file_path, mode='r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())


@auth
def goods():
    """
    浏览并购买
    :return:
    """
    shopping_car = {}
    while True:
        goods_list = []
        with open('goods', mode='r', encoding='utf-8') as f:
            for line in f:
                nid, title, price = line.strip().split('|')
                goods_list.append({'id': nid, 'title': title, 'pirce': price})

        for i in range(len(goods_list)):
            print(i + 1, goods_list[i])

        choice = input('请选择(N不在购买):')
        if choice.upper() == 'N':
            # 写入到购物车
            folder_path = os.path.join('shopping_car', CURRENT_USER)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            ctime = datetime.now().strftime('%Y-%m-%d-%H-%M')
            file_path = os.path.join(folder_path, ctime)
            with open(file_path, mode='a', encoding='utf-8') as f:
                # {1: {'title': '飞机', 'price': 1000, 'count': 15}, 8: {'title': '迫击炮', 'price': 1000, 'count': 10}}
                for key, value in shopping_car.items():
                    line = "%s|%s|%s|%s\n" % (key, value['title'], value['price'], value['count'],)
                    f.write(line)
            return

        choice = int(choice)
        number = int(input('请输入数量:'))
        row_dict = goods_list[choice - 1]

        if row_dict['id'] in shopping_car:
            shopping_car[row_dict['id']]['count'] += number
        else:
            shopping_car[row_dict['id']] = {'title': row_dict['title'], 'price': row_dict['pirce'], 'count': number}


def register():
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


def is_frozen(user):
    """
    判断用户是否已经被冻结
    :param user: 要检查的用户名
    :return:
    """
    if not os.path.exists('frozen.txt'):
        return False
    with open('frozen.txt', 'r', encoding='utf-8') as f:
        user_list = f.readlines()
    frozen_user_list = {item.strip() for item in user_list if item.strip()}
    if user in frozen_user_list:
        return True
    return False


def login():
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
        if not os.path.exists('db.txt'):
            print('无用户，请注册！')
            return

        with open('db.txt', mode='r', encoding='utf-8') as f:
            for line in f:
                username, password, ctime = line.split('|')

                if username == user:
                    username_exists = True
                if username == user and password == pwd:
                    flag = True
                    print('登陆成功')
                    global CURRENT_USER
                    CURRENT_USER = user
                    return

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
    func_dict = {'1': register, '2': login, '3': goods, '4': car}
    while True:
        print('1.用户注册;2.用户登录;3.商品浏览;4.我的购物车')
        choice = input('请选择:')
        func = func_dict.get(choice)
        if not func:
            print('选择错误')
            continue
        func()


if __name__ == '__main__':
    run()
