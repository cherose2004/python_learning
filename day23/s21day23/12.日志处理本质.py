#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging

file_handler1 = logging.FileHandler('x2.log', 'a', encoding='utf-8')
fmt1 = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
file_handler1.setFormatter(fmt1)

# file_handler2 = logging.FileHandler('x2.log', 'a', encoding='utf-8')
# fmt2 = logging.Formatter(fmt="%(asctime)s:  %(message)s")
# file_handler2.setFormatter(fmt2)

logger = logging.Logger('xxxxxx', level=logging.ERROR)
logger.addHandler(file_handler1)
# logger.addHandler(file_handler2)



logger.error('你好')