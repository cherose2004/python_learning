#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def f1():
    sys.exit(0)
    print(1)
    return
    print(123)


def f2():
    print(456)


f1()

f2()