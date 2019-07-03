#!/usr/bin/env python
# -*- coding:utf-8 -*-

# x = 10
# def func():
#     x = 9
#     print(x)
#     def x1():
#         x = 999
#         print(x)
#
# func()



# x = 10
# def func():
#     x = 9
#     print(x)
#     def x1():
#         x = 999
#         print(x)
#     x1()
#
# func()


# x = 10
# def func():
#     x = 9
#     print(x)
#     def x1():
#         x = 999
#         print(x)
#     print(x)
#     x1()
#
# func()

# x = 10
# def func():
#     x = 8
#     print(x)
#     def x1():
#         x = 999
#         print(x)
#     x1()
#     print(x)
#
# func()


# x = 10
# def func():
#     x = 8
#     print(x)
#     def x1():
#         print(x)
#     x1()
#     print(x)
#
# func()



# x = 10
# def func():
#     x = 8
#     print(x)
#     def x1():
#         print(x)
#     x = 9
#     x1()
#     x = 10
#     print(x)
#
# func()

#
# x = 10
# def func():
#     x = 8
#     print(x)
#     def x1():
#         print(x)
#
#     x1()
#     x = 9
#     x1()
#     x = 10
#     print(x)
#
# func()


# name = 'oldboy'
# def func():
#     name = 'alex' # 在自己作用域再创建一个这样的值。
#     print(name)
# func()
# print(name)

name = "老男孩"
def func():
    name = 'alex'
    def inner():
        name = 999
        def test():
            nonlocal name
            name = '888'
        test()
    inner()
    print(name)
func()
print(name)