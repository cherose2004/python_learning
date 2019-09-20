#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import hmac
secret_key = b'alexsb'
random_seq = os.urandom(32)
hmac = hmac.new(secret_key,random_seq)
ret = hmac.digest()
print(len(ret))










