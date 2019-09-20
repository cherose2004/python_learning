王胜辉

麒麟 

集群系统



### 安装centos

- 直接在机器上安装
- 双系统
- 通过虚拟软件在windows上安装linux

### 虚拟软件：通过软件来模拟生成硬件信息

- vmvare
- vbox
- mac

桥接：会跟你的windows机器获取同一个网段的ip地址

net：不会跟windows机器获取同一个网段的ip地址

2^32

2^64

密码要求：

- 12位及其以上
- 必须包含大写字母，小写字母，数字，特殊字符
- 3个月或者半年更换一次

弱口令： 



### linux用户

- root 用户
  - 超级管理员
  - 对系统有完全操作的权限
  - 误操作对系统的损害无限大
  - 尽量不要使用root登录
- 普通用户
  - 对系统的操作权限很小
  - 损害有限
  - 需要用普通用户登录

### 终端

- 图形终端
- 虚拟终端（）ctrl+alt+F1-6  /dev/tty#
- 物理终端
- 设备终端
- 串行终端
- 伪终端  /dev/pts/#
- tty 查看命令

### 远程连接工具

- xshell
- putty
- securecrt

命令

### 查看ip地址

```SHELL
ifconfig 查看ip地址
ip addr 
ip a
```

### 交互式接口

启动终端以后，在终端设备上会打开一个接口

- GUI 图形接口
- CLI
  - shell
  - powershell

### shell

用来在linux系统上的一个接口，用来将用户的输入发送给操作系统去执行，并把得到的结果输出出来

查看系统支持的shell cat  /etc/shells 

切换shell chsh -s shell

查看当前运行的shell echo $SHELL

### 命令提示符

```SHELL
[root@localhost ~]# 
# 超级管理员
$ 普通用户
[用户@主机名 目录]命令提示符
永久生效
echo 'PS1="\[\e[1;30;35m\][\u@\h \W]\\$\[\e[0m\]"' >> /etc/profile.d/ps.sh 
```

### 执行命令

写完命令后直接回车就可以

- 内部命令

  安装完系统以后自带的命令，就是内部命令

  通过help来获取内部命令的列表

- 外部命令

  - 第三方提供的，在某些地方可以直接找到执行文件

```SHELL
type 查看命令的类型
which 查找命令的路径
```

### alias 别名

```SHELL
alias 直接列出了系统里面所有的别名
alias cdetc='cd /etc' 设置别名
unalias cdetc 取消别名
#让命令一致生效
#对当前用户
[root@localhost ~]#echo "alias cdetc='cd /etc'" >> .bashrc
#对所有的用户都生效
echo "alias cdetc='cd /etc'" >> /etc/bashrc
ls 相当于list

```

### 执行原来本身的命令

- "ls"
- \ls
- 'ls'

### 单双引号的区别

"" 可以直接打印变量的值

'' 引号里面写什么就打印什么

### date

```SHELL
[root@localhost ~]#date
Mon Jul 29 12:18:14 CST 2019
[root@localhost ~]#date +%F
2019-07-29
[root@localhost ~]#date +%H（24小时制）
12
[root@localhost ~]#date +%I（12小时制）
12
[root@localhost ~]#date +%y
19
[root@localhost ~]#date +%m
07
[root@localhost ~]#date +%d
29
[root@localhost ~]#date +%M
22
[root@localhost ~]#date +%S
25
[root@localhost ~]#date +%a
Mon
[root@localhost ~]#date +%A
Monday
[root@localhost ~]#date +%T
12:23:31
[root@localhost ~]#date +%y-%m-%d
19-07-29
[root@localhost ~]#date +%Y-%m-%d
2019-07-29
unix元年
[root@localhost ~]#date +%s 时间戳
1564374331
[root@localhost ~]#date +%W 一年中的多少周
30
```

### 时区

```SHELL
[root@localhost ~]#timedatectl
[root@localhost ~]#timedatectl set-timezone  Asia/Shanghai
```

### 日历

```SHELL
cal 展示当月的日历
cal -y 展示当年的日历
cal -y # 显示#年的日历
```

### 关机重启

```SH
shutdown 默认是一分钟之后关机
shutdown -c 取消
shutdown -r 重启
TIME
	- now  立即
	hh：mm
	+# 表示多长时间以后重启
reboot 重启
       -p 切断电源
init 6 重启
init 0 关机
poweroff 关机

```

### 命令的格式

```SHELL
command [options] [args...]
选项：启用或者禁用某些功能的
	短选项：-a
	长选项：--all
参数：命令的作用对象，一般情况是目录，用户等等
注意：
	多个选项及参数和命令之间需要用空格隔开
	ctrl+c来取消命令的执行
	用；来隔开同时执行的多个命令
	使用\来将命令切换成多行
```
