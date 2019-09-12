# -*- coding: utf-8 -*-
# __author__ = "maple"

class HashTable(object):
    def __init__(self,size=999):
        self.container = [ [] for item in range(size)]
        self.size = size

    def add(self,key,value):
        """
        在哈希表中添加数据
        :param key:
        :param value:
        :return:
        """
        key_hash_value = abs(hash(key))
        div = key_hash_value % self.size
        self.container[div].append((key,value))

    def get(self,key):
        key_hash_value = abs(hash(key))
        div = key_hash_value % self.size
        data_list = self.container[div]
        for k,v in data_list:
            if key == k:
                return v
h = HashTable()
h.add('LP','中秋节快乐')
h.add('wzy','中秋节不快乐')

value = h.get('LP')
print(value)

