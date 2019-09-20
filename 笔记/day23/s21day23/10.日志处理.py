#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging

logging.basicConfig(
    filename='cmdb1.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.ERROR
)

# 无效
logging.basicConfig(
    filename='cmdb2.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.ERROR
)

logging.error('alex')
