#!/usr/bin/env python
# -*- coding:utf-8 -*-

print([__name__])
if __name__ == '__main__':
    # 控制当这个py文件被当作脚本直接执行的时候，就执行这里面的代码
    # 当这个py文件被当作模块导入的时候，就不执行这里面的代码
    print('hello hello')
# __name__ == '__main__'
    # 执行的文件就是__name__所在的文件
# __name__ == '文件名'
    # __name__所在的文件被导入执行的时候