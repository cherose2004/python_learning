#!/usr/bin/env python
# -*- coding:utf-8 -*-

# obj = dict()
# obj['k1'] = 123
# del obj['k1']

class Foo(object):

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        return item + 'uuu'

    def __delitem__(self, key):
        pass


obj1 = Foo()
obj1['k1'] = 123  # 内部会自动调用 __setitem__方法
val = obj1['xxx']  # 内部会自动调用 __getitem__方法
print(val)
del obj1['ttt']  # 内部会自动调用 __delitem__ 方法
