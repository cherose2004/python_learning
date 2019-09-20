#!/usr/bin/env python
# -*- coding:utf-8 -*-
# msg = "我是%s,年龄%s" %('alex',19,)
# print(msg)

# msg = "我是%(n1)s,年龄%(n2)s" % {'n1': 'alex', 'n2': 123, }
# print(msg)







# v1 = "我是{0},年龄{1}".format('alex',19)
v1 = "我是{0},年龄{1}".format(*('alex',19,))
print(v1)

# v2 = "我是{name},年龄{age}".format(name='alex',age=18)
v2 = "我是{name},年龄{age}".format(**{'name':'alex','age':18})
print(v2)

