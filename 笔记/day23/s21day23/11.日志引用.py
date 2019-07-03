#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import requests

logging.basicConfig(
    filename='wf.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.ERROR
)

try:
    requests.get('http://www.xxx.com')
except Exception as e:
    msg = str(e) # 调用e.__str__方法
    logging.error(msg,exc_info=True)
