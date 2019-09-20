# -*- coding: utf-8 -*-
# __author__ = "maple"

# 操作系统提供
# 为了提高网络操作的并发效果，并且减少CPU的使用率才被推出的一个工具
# select poll epoll
# windows select
# linux select poll epoll
import socket
import select

sk = socket.socket()
sk.setblocking(False)
sk.bind(('127.0.0.1',9000))
sk.listen()

rlst = [sk]
while True:
    rl,wl,el = select.select(rlst,[],[])
    print('-->',rl)
    for obj in rl:
        if obj is sk:
            conn,_ = obj.accept()
            rlst.append(conn)
        else:
            msg = obj.recv(1024)
            if msg:
                print(msg)
                obj.send(msg)
            else:
                rlst.remove(obj)


# 为什么叫IO多路复用 ：操作系统提供的 网络对象监听的代理
# select 机制是怎么实现的
    # 操作系统会帮助程序对需要监听的所有对象进行轮询
    # 一旦有数据来，就会把对应的对象返回
    # select
        # 由于底层数据结构的问题，select能够代理的网络对象是有限的
        # 随着监听的对象增多 效率也会降低
# poll 机制
    # 轮询 随着监听的对象增多 效率也会降低
    # 对底层数据结构进行了优化 能够代理的网络对象没有限制了
# epoll 机制
    # 不再采用轮询的机制 采用的是回调机制
    # 无论监听多少个网络对象，效率都是一样的

import selectors












