#!/usr/bin/env python
# -*- coding:utf-8 -*-

# class Foo:
# #     pass
# #
# # obj = Foo()
# #
# # if type(obj) == Foo:
# #     print('obj是Foo类的对象')

# class Base:
# #     pass
# #
# # class Base1(Base):
# #     pass
# #
# # class Foo(Base1):
# #     pass
# #
# # class Bar:
# #     pass
# #
# # print(issubclass(Bar,Base))
# # print(issubclass(Foo,Base))
"""
class Base(object):
    pass

class Foo(Base):
    pass

obj = Foo()

print(isinstance(obj,Foo)) # 判断obj是否是Foo类或其基类的实例（对象）
print(isinstance(obj,Base)) # 判断obj是否是Foo类或其基类的实例（对象）

"""

class Base(object):
    pass
class Foo(Base):
    pass
obj = Foo()
if type(obj) == Foo: # 判断obj是否是Foo类的实例（对象）
    print('obj是Foo类的对象')



