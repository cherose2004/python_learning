# -*- coding: utf-8 -*-
# __author__ = "maple"

"""
from types import MethodType,FunctionType

def func():
    pass

class Foo:
    def f1(self):
        pass

obj = Foo()


print(isinstance(func,FunctionType)) # True
print(isinstance(obj.f1,MethodType)) # True
"""







#
# class Foo:
#     def f1(self):
#         pass
#
# obj = Foo()
# obj.f1  # 方法
#
#
# Foo.f1 # 函数






class Foo:
    def f1(self):
        pass

obj = Foo()
Foo.f1(obj) # 类.xx  -> 函数

obj = Foo()
obj.f1() # 对象.xx -> 方法







