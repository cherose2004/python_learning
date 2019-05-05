#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
def wrapper(func):
    def inner(*args,**kwargs):
        # 检查路径是否存在
        path = args[0]
        if not os.path.exists(path):
            # 路径不存在
            print('路径不存在')
            return None
        result = func(*args,**kwargs)
        return result
    return inner

@wrapper
def read_userinfo(path):
    file_obj = open(path,mode='r',encoding='utf-8')
    data = file_obj.read()
    file_obj.close()
    return data

content = read_userinfo('/usr/bin/xxx/xxx')
print(content)