#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo:

    @property
    def func(self):
        print(123)
        return 666


obj = Foo()

result = obj.func
print(result)