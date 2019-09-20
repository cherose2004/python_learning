## 计划任务

at 可以来做一次性的任务

crontab

- 同步时间
- 备份
- 日志

```*
SHELL=/bin/bash                                                                                                          
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

分钟  小时  天  月 周 用户  命令
* * * * * root touch /tmp/a.txt

* 代表所有
* * * * * root echo "1" >> /tmp/a.txt 每分钟做什么事
0 * * * * root echo "0" >> /tmp/b.txt 每个小时的第0分钟做什么事
0 4 3 * * root echo "0" >> /tmp/c.txt
0 4 * * 4 root echo "0" >> /tmp/c.txt
0 4,6,8 * * * root echo "0" >> /tmp/d.txt  每天的4,6,8点的时候做什么事
0 8-22 * * *  root echo "上课" >> /tmp/f.txt 每天的早上8点到22点做什么事
0 8-22/3 * * * root echo "休息" >> /tmp/e.txt  每天的早上8点到22点每隔3个小时做什么事
41 *  3,15,25,30 * 6 echo "da" >> /tmp/g.txt  每个月的3,15,25,30 或者每周6做什么事 (特殊的)

* 代表所有
#1,#2,#3 #1或者#2或者#3
#1-#2 #1到#2
/# 每隔#时间
```

## crontab

```SHELL
-u 指定用户 默认是当前用户
-e  编辑
-l 列出
-r 删除
不是真正的存在/etc/crontab,而是存在/var/spool/cron/,这个目录下会为每一个用户创建一个文件
```

建议大家

- 分钟不要用*
- 分钟不要用*
- 分钟不要用*

## ip地址的分类

ip总共多少位?  有多少段? 

一个段是8位 总共32位

又分为网络位和主机位

192.168.182.128

192.168.182 这个网段

128 主机位 ,可以通过主机来判断当前的网段内可以放多少台终端

A

前8位为网络位,后24位为主机位

0  0000000

0  1111111

1-126 

127 为回环地址

可用网段 2^7-1

主机 2^24

主机位全为0,表示网段

主机位全为1,网段里面的广播地址

可用ip是多少?2^24-2

共有地址: 所有人都可以访问的地址

私有地址:只能内部访问的地址

10 

B

前16位为网络位,后16位为主机位

10 000000 00000000  128

10 111111 11111111  191

可用网段: 2^14

可用ip: 2^16-2

私有地址

172.16-172.31

C

前24位为网络位,后8位为主机位

110 00000  0  0 

110 11111 255 255

192

223 

可用网段 2^21

可用ip地址 2^8-2

私有网段

192.168.0

192.168.255

D 广播 多播的地址

1110 0000

224

1110 1111

239

E 留作科研使用

240-254

CIDR(无类域间路由)

网络位向主机位借位

前30位网络位

后2位为主机位

ip地址/子网掩码 与运算

子网掩码 网络位全为1,主机位全为0

192.168.182.129/24

1100 0000  1010 1000‬ 1011 0110‬   1000 0001‬

255.255.255.0

11111111  11111111   11111111    00000000

192.168.182.0

与 全为1才位1,只要有0则为0

或  有1则为,全为0才为0

异或 相同为0,不同为1

取反 -(n+1)

左移 2<<2      n*2位移倍数次方

右移12>>2   n/2位移倍数次方 向下取正

10.23.34.56/15

10.00010111.34.56

0000 1010 00010111 

1111 1111 11111110

10.22.0.0

可用ip地址:2^17-2



## ip的获取方式

手动

dhcp服务器 分配ip地址

## 手动设置

ifconfig

ip

```shell
ip addr add 192.168.182.200/24 dev ens33
ip a add 192.168.182.245/24 dev ens33 label ens33:0
ip a del 192.168.182.200/24 dev ens33
ip a del 192.168.182.20/24 dev ens33 label ens33:1
```

网卡配置

```shell
TYPE=Ethernet            网卡的接口类型:     Ethernet Bridge
PROXY_METHOD=none  
BROWSER_ONLY=no
BOOTPROTO=dhcp  获取ip地址的协议: dhcp none static    
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33   网卡名称
UUID=04faa6f8-44e8-479a-aa55-2df5783ce516  uuid
DEVICE=ens33   设备
ONBOOT=yes   开机是否自启动
IPADDR=192.168.182.130 ip地址
NETMASK= 255.255.255.0 子网掩码
GATEWAY= 192.168.182.2 网管
DNS1=114.114.114.114 dns1
DNS2=8.8.8.8 dns2

```

/etc/resolv.conf 存放dns的配置文件

## hostname

查看或者修改主机名

 /etc/hostname 配置文件

临时有效:

​	hostname name

永久有效:

	-	修改配置文件
	-	hostnamectl set-hostname name

## 本地解析

可以写主机和ip地址的映射关系

并且先检查此文件

/etc/hosts

## ss\netstat

打印网络系统的状态

```SHELL
-t tcp 
-u udp
-x 套接字
-a 所有
-l 处于监听的
-p 相关的程序及pid
-n 显示端口
22 ssh
http 80
mysql 3306
redis 6379
mongdb 27017
windows远程桌面 3389
oracle数据库 1521
https 443
ftp  20    21
常用的组合: -tnlp -aulp -tan
```

## wget

下载文件

```SHELL
-O filename 指定生成的文件名
-P 保存到指定的目录
-q 静默模式
-r 递归下载
-p 下载所有的html元素
wget http://www.xiaohuar.com/d/file/20190809/small620192446e4599c844fc40a3e7b119141565366028.jpg
wget -P /tmp http://www.xiaohuar.com/d/file/20190809/small620192446e4599c844fc40a3e7b119141565366028.jpg
wget -O /tmp/xiaohua.png http://www.xiaohuar.com/d/file/20190809/small620192446e4599c844fc40a3e7b119141565366028.jpg
wget -p http://www.xiaohuar.com/
wget -q -O /tmp/xiaohua2.png http://www.xiaohuar.com/d/file/20190809/small620192446e4599c844fc40a3e7b119141565366028.jpg
其中 -P 和-O 选项冲突
```

## ps

查看进程

支持的方式

- unix格式 -a -e
- BSD格式   aux
- GNU格式  --help

```shell
默认显示的是当前终端上的进程
a 显示所有终端的进程
x 显示不连接终端的进程
u 展示进程的所有者信息
f 显示进程树
o 按照指定的属性来显示信息
L 显示所有的属性
k 用来排序,后面执行排序的属性,如果需要倒叙的话,属性前面加上-
-e 显示所有的进程
-f 显示完整的信息
-U username 用来指定用户
常用组合: aux -ef
需要跟grep做结合

```

## pidof

跟进名称来查进程

## 进程管理工具

### kill

向进程发送信号,实现对进程的管理,每个信号都有不同的数字对应,

常用信号:

	-	1 : sighup 重读配置文件
	-	2: sigint 终止正在运行的进程,相当于ctrl+c
	-	9:sigkill 强制杀死正在运行的进程
	-	19:sigstop:后台休眠
	-	18:sigcont 继续运行



按照pid kill pid

按照名称  killall name 

按照模式 pkill name  



## 系统工具

### uptime

- 显示当前时间,系统开启的时长,当前在线的人数,系统的平均负载(1分钟,5分钟,15分钟)
- 平均负载:在特定的时间内cpu上等待运行的进程数
- 如果不超过cpu核心数的2倍则认为是良好的

### top

排序

- P 按照cpu排序
- M 按照内存排序
- T 按照占用cpu的时长,TIME+

首部信息显示

- uptime信息:l
- tasks和cpu信息:t
- 内存信息:m
- 分别显示cpu信息:1(数字)
- 修改刷新时间 s
- 杀死正在运行的进程 k
- 退出 q

选项:

- -d # 指定刷新时间
- -b 显示所有的进程
- -n # 刷新多少次以后退出

### htop

在epel源

##  性能分析工具

### free

```shel
-m 以mb的方式显示
-g 以GB的方式显示
-h 易读格式
-s n 指定刷新频率
-c n 刷新n次后退出
```

vmstat

```shell
vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 3  0      0 341948   2152 733492    0    0    21     2   68   70  0  1 99  0  0
procs:
r 可运行(正在运行或者等待运行)的进程个数
b处于不可中断的进程个数(被阻塞的队列长度)
memory:
swpd 交换内存的使用量
free 空闲内存的总量
buff 用于buffer的内存总量
cache 用于cache的内存总量
swap
si 从磁盘交换到内存的数据速率(kb/s)
so 从内存到磁盘的数据的速率(kb/s)
io
bi: 从块设备读入数据到系统的速率
bo: 从系统到块设备
cpu
us 用户空间
sy 系统空间
id 空闲
wa 等待
st 被偷走的时间
```

## 作业管理

后台运行

- ctrl +z
- command & 会输出到屏幕
- nohup command & 不会输出到屏幕

## systemctl

管理服务的

systemctl   参数   服务

systemctl  start  sshd nginx  redis 启动

stop 停止

restart  重启

reload 重新加载配置文件

status 查看服务的状态

enable 开机自启动

disable 关闭开机自启动

systemctl list-unit-files |grep enabled 查询那些服务是开机自启动的

## iptables

firewall

iptables -F 清空防火墙规则

## selinux

setenforce 0   临时关闭

getenforce  查看selinux的状态

配置文件在/etc/selinux/config

SELINUX=disabled



## 虚拟环境

python3 创建虚拟环境

```shell
python3 -m venv name 在当前目录下生成一个文件夹
source name/bin/activate 进入虚拟环境
deactivate 退出虚拟环境
```

python2 管理虚拟环境

```SHELL
pip install virtualenv -i https://pypi.douban.com/simple
```

生成虚拟环境

```shell
virtualenv --no-site-packages --python=python test
--no-site-packages 生成一个干净的虚拟环境
--python 用来指定以哪个python来生成虚拟环境
```

## 确保环境一致

```shell
在windows执行
pip freeze > requirements.txt
把文件传到linux上面
切换虚拟环境
pip install -r requirements.txt
```

## virtualenvwrapper

```SHELL
export WORKON_HOME=~/Envs   #设置virtualenv的统一管理目录
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'   #添加virtualenvwrapper的参数，生成干净隔绝的环境
export VIRTUALENVWRAPPER_PYTHON=/opt/python347/bin/python3     #指定python解释器
source /opt/python34/bin/virtualenvwrapper.sh #执行virtualenvwrapper安装脚本
读取文件，使得生效，此时已经可以使用virtalenvwrapper
source .bashrc  
加载.bashrc文件
```

使用

```SHELL
mkvirtualenv django3 创建虚拟环境并进入
lsvirtualenv  列出所有的虚拟环境
workon 直接切换虚拟环境
cdvirtualenv 直接切换到虚拟环境
cdsitepackages 切换到虚拟环境的三方包
lssitepackages 列出当前虚拟环境的三方包
rmvirtualenv 删除虚拟环境
deactivate 退出虚拟环境
```



nginx   apache engine

redis  关系型数据 nosql  no only sql

docker 容器

rabbitmq  消息队列

saltstack  ansible puppet fabric    openstack(私有云)

淘宝 java 

新美大

go





人肉运维

半自动化运维

zabbix

普罗米修斯

自动化运维

AI运维









