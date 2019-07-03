#!/usr/bin/env python
# -*- coding:utf-8 -*-

# class Foo(object):
#     def __enter__(self):
#         self.x = open('a.txt',mode='a',encoding='utf-8')
#         return self.x
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.x.close()
#
# with Foo() as ff:
#     ff.write('alex')
#     ff.write('alex')
#     ff.write('alex')
#     ff.write('alex')



# class Context:
#     def __enter__(self):
#         print('进入')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('推出')
#
#     def do_something(self):
#         print('内部执行')
#
# with Context() as ctx:
#     print('内部执行')
#     ctx.do_something()


class Foo(object):
    def do_something(self):
        print('内部执行')

class Context:
    def __enter__(self):
        print('进入')
        return Foo()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('推出')


with Context() as ctx:
    print('内部执行')
    ctx.do_something()
