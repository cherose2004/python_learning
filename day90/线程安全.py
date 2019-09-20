import time
from threading import local
import threading

rom = {
    2800:{"foo.num":0},
    14096:{"foo.num":1},
    12388:{"foo.num":2}
}


class Foo(local):
    num = 0

foo = Foo()
def addi(i):
    foo.num = i
    time.sleep(0.5)  # 相当于IO操作
    print(foo.num,threading.currentThread().ident)

from threading import Thread
for i in range(20):
    task = Thread(target=addi,args=(i,))
    task.start()

