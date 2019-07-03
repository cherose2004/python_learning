#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 网络编程
# B/S和C/S架构
    # C/S   ftp
    # B/S   网页开发
# osi五层协议
    # 应用层 python
    # socket/socketserver
    # 传输层 端口/服务相关   四层交换机 四层路由器
        # tcp/udp协议
            # tcp协议 ：面向连接的 可靠的 全双工的 流式传输协议
                # 三次握手
                # 四次挥手
                # 粘包现象
                    # 在接收端粘
                        # 发送信息无边界 在接收端没有及时接收 在缓存端黏在一起
                    # 在发送端粘
                        # 消息短 时间间隔小 由于优化机制粘在一起
                # 拆包机制
            # udp协议 ：面向数据报的 不可靠 无连接的协议
    # 网络层  ip相关
        # ipv4 ipv6   路由器 三层交换机
    # 数据链路层  mac相关
        # arp    网卡  交换机
    # 物理层
# I/O操作 输入和输出
    # input 输入到内存  recv recvfrom
    # output 从内存输出 send sendto
# 阻塞和非阻塞
    # 阻塞 ：cpu不工作 accept recv connect 等待
    # 非阻塞 ：cpu工作

# socket模块
    # tcp协议
        # 服务端 客户端
        # 粘包问题 ：struct模块
    # udp协议
        # 服务端 客户端
# socketserver模块
# hamc模块  —— 校验客户端的合法性













