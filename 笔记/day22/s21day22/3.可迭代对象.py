#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Foo:
    def __iter__(self):
        yield 1
        yield 2
        yield 3

obj = Foo()

for item in obj:
    print(item)