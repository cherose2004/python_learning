# -*- coding: utf-8 -*-
# __author__ = "maple"


import functools


def f1(a1,a2,a3):
    print(a1,a2,a3)
new_f1 = functools.partial(f1,a1=123)
new_f1()



"""
def outer(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@outer
def home():
    print('home')

def index():
    print('index')

print(home.__name__) # home() 执行的inner，
print(index.__name__)
"""