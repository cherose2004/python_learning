#!/usr/bin/env python
# -*- coding:utf-8 -*-

url = 'https://www3.autoimg.cn/newsdfs/g3/M07/F0/1D/120x90_0_autohomecar__ChcCRVynRb6AM6guAADLT7nJgC0929.jpg'


import requests

r1 = requests.get(url)
f = open('v1.jpg',mode='wb')
f.write(r1.content)
f.close()