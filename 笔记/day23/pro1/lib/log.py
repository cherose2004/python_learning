#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import logging
from logging import handlers
from config import settings


def get_logger():
    # file_handler = logging.FileHandler(filename=os.path.join(settings.BASE_DIR,'log',settings.LOG_FILE_NAME), mode='a', encoding='utf-8',)
    file_handler = handlers.TimedRotatingFileHandler(filename=settings.LOG_FILE_PATH,
                                                     when=settings.LOG_WHEN,
                                                     interval=settings.LOG_INTERVAL,
                                                     encoding='utf-8')
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p',
        handlers=[file_handler,],
        level=logging.ERROR
    )
    return logging

logger = get_logger()

