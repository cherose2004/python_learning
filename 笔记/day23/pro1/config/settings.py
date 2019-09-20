#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE_PATH = os.path.join(BASE_DIR,'log','cmdb.log')
LOG_WHEN = "s"
LOG_INTERVAL = 5