# -*- coding: utf-8 -*-
# __author__ = "maple"

# import requests
#
# requests.get('http://www.baidu.com')

d={"a":26,"g":20,"e":20,"c":24,"d":23,"f":21,"b":25}
print(sorted(d.items(),key=lambda x:x[1]))