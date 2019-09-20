#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process

class MyProcecss2(Process):
    def run(self):
        while True:
            print('is alive')
            time.sleep(0.5)

class MyProcecss1(Process):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__()
    def run(self):
        print(self.x,self.y,os.getpid())
        for i in range(5):
            print('in son2')
            time.sleep(1)

if __name__ == '__main__':
    mp = MyProcecss1(1,2)
    mp.daemon = True
    mp.start()
    print(mp.is_alive())
    mp.terminate()
    # mp2 = MyProcecss2()
    # mp2.start()
    # print('main :',os.getpid())
    # time.sleep(1)