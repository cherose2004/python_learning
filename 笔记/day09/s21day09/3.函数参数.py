#!/usr/bin/env python
# -*- coding:utf-8 -*-

def send_email(to):
    template = "要给%s发送邮件" % (to,)
    print(template)


user_input = input('请输入角色：')

if user_input == '管理员':
    send_email('xxxx@qq.com')
elif user_input == '业务员':
    send_email('xxxxo@qq.com')
elif user_input == '老板':
    send_email('xoxox@qq.com')