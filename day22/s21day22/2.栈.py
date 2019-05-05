#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
class Stack(object):
    """
    后进先出
    """
    def __init__(self):
        self.data_list = []

    def push(self, val):
        """
        向栈中压入一个数据（入栈）
        :param val:
        :return:
        """
        self.data_list.append(val)

    def pop(self):
        """
        从栈中拿走一个数据（出栈）
        :return:
        """
        return self.data_list.pop()
#
# obj = Stack()
# obj.push('alex')
# obj.push('eric')
# obj.push('杀杀杀')
#
# v1 = obj.pop()
# print(v1)
# v2 = obj.pop()
# print(v2)
# v3 = obj.pop()
# print(v3)

#
# class Stack(object):
#     """
#     后进先出
#     """
#     def __init__(self):
#         self.data_list = []
#
#     def push(self, val):
#         """
#         向栈中压入一个数据（入栈）
#         :param val:
#         :return:
#         """
#         self.data_list.insert(0,val)
#
#     def pop(self):
#         """
#         从栈中拿走一个数据（出栈）
#         :return:
#         """
#         return self.data_list.pop(0)