#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lib.log import logger

def login():
    print('登陆')
    try:
        int('asdf')
    except Exception as e:
        logger.error(str(e),exc_info=1)

def register():
    print('注册')
    logger.error('asdf')
