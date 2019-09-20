#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# 可变
- 浅拷贝：拷贝第一层
- 深拷贝：拷贝所有数据
"""
"""
# 应该每次都拷贝一份（但由于小数据池，未拷贝）
v1 = 'alex'
import copy
v2 = copy.copy(v1)
print(id(v1),id(v2))

v3 = copy.deepcopy(v1)
print(id(v1),id(v3))
"""
"""
v1 = [1,2,3,4]
import copy
v2 = copy.copy(v1)
print(id(v1),id(v2))

v3 = copy.deepcopy(v1)
print(id(v1),id(v3))
"""

# v1 = [1,2,3,4,[11,22,33]]
# import copy
# v2 = copy.copy(v1)
# print(id(v1),id(v2))
# print(id(v1[4]),id(v2[4]))

# v2 = copy.deepcopy(v1)
# print(id(v1),id(v2))
# print(id(v1[4]),id(v2[4]))


# ###################################################
# 练习 1
"""
import copy
v1 = [1,2,3]
v2 = copy.copy(v1)
print(v1 == v2) # True
print(v1 is v2) # False
print(v1[0] is v2[0]) # True
"""
# 练习 2
"""
import copy
v1 = [1,2,3]
v2 = copy.deepcopy(v1)
print(v1 == v2) # True
print(v1 is v2) # False
print(v1[0] is v2[0]) # True
"""
### 练习3
"""
import copy
v1 = [1,2,3,{'k1':123,'k2':456}]
v2 = copy.deepcopy(v1)
print(v1 == v2) # True
print(v1 is v2) # False
print(v1[0] is v2[0]) # True
print(v1[3] == v2[3]) # True
print(v1[3] is v2[3]) # False
"""
# ################ 总结 #########################
# 浅拷贝：只拷贝第一层。
# 深拷贝：拷贝嵌套层次中的所有可变类型。
# ------ 特殊情况
"""
v1 = (1,2,3,4)

import copy
v2 = copy.copy(v1)
print(id(v1),id(v2))
v3 = copy.deepcopy(v1)
print(id(v1),id(v3))
"""

"""
v1 = (1,2,3,[1,2,3],4)
import copy
v2 = copy.copy(v1)
print(id(v1),id(v2))
v3 = copy.deepcopy(v1)
print(id(v1),id(v3))
"""


# 不可变
# v1 = 'asdf'
# v1 = 123
# import copy
# v2 = copy.copy(v1)
# print(id(v1),id(v2))
# v3 = copy.deepcopy(v1)
# print(id(v1),id(v3))

# 可变 + 不可变
"""
v1 = [1,2,3,[11,2,33]]
import copy
v2 = copy.copy(v1)
print(id(v1),id(v2))
v3 = copy.deepcopy(v1)
print(id(v1),id(v3))
"""