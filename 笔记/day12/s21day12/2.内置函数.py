#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

def get_random_code(length=6):
    data = []
    for i in range(length):
        v = random.randint(65,90)
        data.append(chr(v))

    return  ''.join(data)


code = get_random_code()
print(code)