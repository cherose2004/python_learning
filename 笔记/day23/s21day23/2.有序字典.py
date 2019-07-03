#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import OrderedDict

info = OrderedDict()
info['k1'] = 123 # __setitem__
info['k2'] = 456
# info['k1']       # __getitem__

print(info.keys())
print(info.values())
print(info.items())

