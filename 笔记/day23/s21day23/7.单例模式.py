#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ############################### 多例 ##################################
# class Foo:
#     pass
#
# obj1 = Foo() # 实例，对象
# obj2 = Foo() # 实例，对象
#
# print(obj1,obj2)

# ############################### 单例 ##################################


class Singleton(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        # if Foo.instance:
        #     return Foo.instance
        # Foo.instance = object.__new__(cls)
        # return Foo.instance
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

obj1 = Singleton()
obj2 = Singleton()