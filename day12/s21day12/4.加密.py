#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
USER_LIST = []
def get_md5(data):
    obj = hashlib.md5("12:;idrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result


def register():
    print('**************用户注册**************')
    while True:
        user = input('请输入用户名:')
        if user == 'N':
            return
        pwd = input('请输入密码:')
        temp = {'username':user,'password':get_md5(pwd)}
        USER_LIST.append(temp)

def login():
    print('**************用户登陆**************')
    user = input('请输入用户名:')
    pwd = input('请输入密码:')

    for item in USER_LIST:
        if item['username'] == user and item['password'] == get_md5(pwd):
            return True


register()
result = login()
if result:
    print('登陆成功')
else:
    print('登陆失败')