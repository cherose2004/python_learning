#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from threading import Lock
class A:
    __instance = None
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(0.1)
                cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,name,age):
        self.name = name
        self.age = age

def func():
    a = A('alex', 84)
    print(a)

from threading import Thread
for i in range(10):
    t = Thread(target=func)
    t.start()