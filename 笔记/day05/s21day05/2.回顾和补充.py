#!/usr/bin/env python
# -*- coding:utf-8 -*-

# "".jon([元素必须是字符串,元素必须是字符串,])
nums = [11,22,33,44]
for i in range(0,len(nums)):
    nums[i] = str(nums[i])
resutl = '_'.join(nums)
print(resutl)
