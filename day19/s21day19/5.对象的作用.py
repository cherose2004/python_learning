#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
class File:
    def read(self,path):
        with open(path,mode='r',encoding='utf-8') as f:
            data = f.read()
        return data
    def write(self,path,content):
        with open(path, mode='a', encoding='utf-8') as f:
            f.write(content)

# 实例化了一个File类的对象
obj = File()
obj.read('test.log')
obj.write('test.log','alex')
"""

class File:
    def read(self):
        with open(self.xxxxx, mode='r', encoding='utf-8') as f:
            data = f.read()
        return data

    def write(self, content):
        with open(self.xxxxx, mode='a', encoding='utf-8') as f:
            f.write(content)

# # 实例化了一个File类的对象
obj1 = File()
# # 在对象中写了一个xxxxx = 'test.log'
obj1.xxxxx = "test.log"
# # 通过对象调用类中的read方法，read方法中的self就是obj。
# # obj1.read()
obj1.write('alex')


# 实例化了一个File类的对象
obj2 = File()
# 在对象中写了一个xxxxx = 'test.log'
obj2.xxxxx = "info.txt"
# 通过对象调用类中的read方法，read方法中的self就是obj。
# obj2.read()
obj2.write('alex')
