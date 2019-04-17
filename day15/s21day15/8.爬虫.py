#!/usr/bin/env python
# -*- coding:utf-8 -*-
# pip install requests


import requests
import json

response = requests.get('https://www.luffycity.com/api/v1/course_sub/category/list/')
data = json.loads(response.text)
print(type(data))
print(data)