
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import struct

ret = struct.pack('i',100000)
print(ret)
print(struct.unpack('i',ret))
ret = struct.pack('i',1)
print(ret)
ret = struct.pack('i',5)
print(ret)
ret = struct.pack('i',10)
print(ret)
ret = struct.pack('i',50)
print(ret)
ret = struct.pack('i',7863)
print(ret)
print(struct.unpack('i',ret))


