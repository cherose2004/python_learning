#!/usr/bin/env python
# -*- coding:utf-8 -*-

# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }

# 三级菜单
    # 递归
# def menu_func(menu):
#     while True:
#         for key in menu:
#             print(key)
#         inp = input('>>>').strip()
#         if inp.upper() == 'Q': return 'q'
#         if inp.upper() == 'B': return 'b'
#         elif menu.get(inp):
#             flag = menu_func(menu[inp])
#             if flag == 'q': return 'q'
# menu_func(menu)
# print('ashkskfhjhflhs')

    # 栈
# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
# lst = [menu]
# while lst:
#     for key in lst[-1]:
#         print(key)
#     inp = input('>>>')   # 北京
#     if inp.upper() == 'Q':break
#     elif inp.upper() == 'B':lst.pop()
#     elif lst[-1].get(inp):
#         lst.append(lst[-1][inp])


# 使用listdir求文件夹的大小
# import os
# lst = [r'D:\code']
# size = 0
# while lst:
#     path = lst.pop()
#     name_lst = os.listdir(path)
#     for name in name_lst:
#         full_path = os.path.join(path,name)
#         if os.path.isdir(full_path):
#             lst.append(full_path)
#         elif os.path.isfile(full_path):
#             size += os.path.getsize(full_path)
# print(size)

# 三级目录  自己创建文件和文件夹 自己去打印每一次while循环过程中lst的变化，把这个题搞清楚