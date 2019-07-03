#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Base(object):
    def __init__(self, name):
        self.name = name

class Foo(Base):
    def __init__(self, name):
        self.name = "于大爷"
        super().__init__(name)
        # super(Foo,self).__init__(name)

obj1 = Foo('alex')
print(obj1.name)