#!/usr/bin/env python
# -*- coding:utf-8 -*-

# from utils import redis
import importlib

middleware_classes = [
    'utils.redis.Redis',
    # 'utils.mysql.MySQL',
    'utils.mongo.Mongo'
]
for path in middleware_classes:
    module_path,class_name = path.rsplit('.',maxsplit=1)
    module_object = importlib.import_module(module_path)# from utils import redis
    cls = getattr(module_object,class_name)
    obj = cls()
    obj.connect()


# # 用字符串的形式导入模块。
# redis = importlib.import_module('utils.redis')
#
# # 用字符串的形式去对象（模块）找到他的成员。
# getattr(redis,'func')()
