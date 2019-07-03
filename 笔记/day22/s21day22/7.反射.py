#!/usr/bin/env python
# -*- coding:utf-8 -*-
import x1


print(x1.NUM)

# v1 = getattr(x1,'NUM')
# print(v1)
# v2 = getattr(x1,'func')
# v2()

v3 = getattr(x1,'Foo') # x1.Foo
print(v3)

v4 = getattr(v3,'X')              # x1.Foo.X

v5 = getattr(v3,'info')              # x1.Foo.info
v5()

obj = v3()
m = getattr(obj,'show')
m()