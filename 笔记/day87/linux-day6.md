# 用户和用户组

- 分类

  - 超级管理员 root  uid 0

  - 普通用户

    - 系统用户： 一般情况下用来启动服务或者运行进程，一般情况下系统用户是不可以登陆

      uid 1-999（centos7）1-499（centos6）

    - 可登陆用户：可以登陆系统的用户

      uid 1000-65535（centos7） 500-65535（centos6）

## useradd

只能用root账号来创建用户

```shell
-d 指定用户的家目录，不能创建在/tmp，默认用户的家目录不需要手动创建
-g 组信息   主组有且只能有一个
-G 指定附加组 可以有多个
-M 不创建家目录
-N 不创建组，默认继承至user组
-r 创建一个系统用户，id从1000依次递减
-s 登录以后使用的shell /sbin/nologin 可以登录看到提示，但是会立马被踢掉
-u 指定uid
/etc/default/useradd 默认的配置文件
-D 显示默认配置
useradd  -D -s /sbin/nologin 修改默认的登录后shell
useradd  -D -b /opt/ 修改默认的家目录
useradd  -D -g 3000 修改默认的组
```

## passwd

```shell
passwd [options] username 用来设置密码
-d 删除用户的密码 不能登录
-l 锁定用户
-u 解锁用户
-e 强制用户下次登录的时候修改密码
-x maxdays 密码的最长有效期
-n mindays 密码的最短有效期 
-w wandays 提前多长时间开始警告用户
-i days 密码过期多长时间以后账户被禁用
--stdin 从标准输入读入数据 echo "password" |passwd --stdin username
```

## chage 

交互式的修改密码的策略

```SHELL
-d 将密码修改时间设置为执行的时间
-E 设置用户的过期时间
-I 密码过期多长会时间以后账户被禁用
-l 显示密码的策略
-m 密码的最短使用期限
-M 密码的最长使用期限
-W 密码过期的警告天数
```

## passwd文件详解

- 用户名
- 密码占位符（x）
- 用户的id
- 组id
- 描述信息
- 家目录
- 登录后shell

## usermode

```shell
-L锁定
-U 解锁
-d 新的家目录不会自己创建，要想创建要使用-m选项
usermod -md /usr/local/alex alexdsb
-g 修改主组
-G 修改附加组
-a 追加附加组
usermod -a -G root alexdsb1
-l 改名
-s 修改登录后的shell 
-u 修改uid
```

## userdel

删除用户

```SHELL
-r  删除用户的时候删除用户的家目录
```

## shadow 文件格式

- 用户名
- 密码：一般情况是sha512加密 $加密方式$盐$加密之后的字符串
- 从1970年1月1日到密码最近一次被修改的时间
- 密码的最少使用期限
- 密码的最大使用期限
- 密码过期多长时间提示用（默认是7天）
- 密码过期多长时间之后被锁定
- 从1970年1月1日算起，多少天之后账户失效

## 切换用户

- su

  - su username 切换用户，切换用户要输入切换到用户密码
  - su - username 完全切换，会切换用户的目录还会切换用户的环境变量
  - root 切换到别的用户不需要输入密码

- su [-] username -c "command"  切换用户执行命令后再退回

- sudo command

  ```SHELL
  用root用户修改/etc/sudoers文件
  加上
  xiaofeng ALL=(ALL（命令）)      NOPASSWD（不需要输入密码）: ALL
  表示一个组
  %wheel  ALL=(ALL)       ALL
  ```

## 用户组

- 超级用户组  root 0
- 普通用户组
  - 系统组  gid 1-999（centos7）1-499（centos6）
  - 可登陆用户组 gid 1000-65535（centos7） 500-65535（centos6）

## groupadd

```SHELL
-g 用来指定gid
-r 用来指定系统组
```

## group文件格式

- 组名
- 密码占位符
- gid
- 以当前组为附加组的用户

## groupmod 

```shell
-g 修改gid
-n 修改组的名称
```

## groupdel

删除用户组

## 登陆远程机器

两种认证方式：

- 用户名+密码
- 用户名+key

使用key登陆

```shell
ssh-keygen 生成key
公钥
私钥
非对称加密
ssh-copy-id 复制key到远程机器
公钥加密私钥解密
```



# 磁盘

mount 用来查看挂载信息

df 查看磁盘占用

​	-h 显示人类可读的信息

du 显示的目录的占用空间

​	-h 显示人类易读的信息

​	-s 显示的是目录本身

du -sh / 显示根的占用情况

du -sh /* 显示根下的每一个目录的占用情况

dd 复制文件生成文件

```shell
dd if=/dev/zero of=/dev/null bs=10M count=2
if input file  
of  output file
bs block size 只能用整数，单位可以是K、M、G、T
count 次数
```

# RAID

## raid0（安装系统）

- 读写速度提升
- 可用空间 N*个数
- 没有容错能力
- 最少需要2块磁盘

## raid1（存放数据）

- 度的能力提升，写的性能稍微有点下架
- 可用空间N
- 有容错能力
- 最少要两块

## raid 5（目前比较流行）

- 读写性能提升
- 可用空间N*（个数-1）
- 有容错能力
- 最多可以坏1块（同时）
- 最少要3块

## raid6

- 读写性能有提高
- 可用空间N*（个数-2）
- 有容错能力
- 最多可以坏2块（同时）
- 最少需要4块

## raid10（土豪）

先做raid1 在做raid0

- 读写性能有提升
- 可用空间N*个数/2
- 有容错能力：一个组里面只能坏一块
- 最少需要4块

## raid01

先做raid0，在做raid1

# 包管理工具

介绍

windows exe

redhat rpm

rpm redhat package manager

yum 自己解决依赖关系

- 包
  - 安装包  yum install 
  - 清除缓存  yum clean
  - 列出所有的包 yum list
  - 更新包 yum update
  - 搜索  yum search
  - 详细信息 yum info
  - 列出yum仓库信息 yum repolist
  - 重新安装 yum reinstall
  - 卸载包 yum remove
  - 检查的依赖关系 yum deplist
  - 重建缓存 yum makecache
  - 搜索指定的命令由那个包生成 yum provides 

- 包组
  - 列出包组 yum group list
  - 安装包组 yum group install
  - 查看包组信息 yum group info
  - 卸载包的信息 yum group remove

rpm 命令

```shell
rpm -q package 检查这个包是否安装
-a 列出所有已经安装的包
-f 查询文件由那个包生成
rpm -qf /etc/redis.conf 
-l  查询包生成的文件
rpm -ql redis
-i 查询包的信息
rpm -qi redis
-c 查找包生成的配置文件
rpm -qc redis
```

包的命名规范	

```shell
python-2.7.5-80.el7_6.x86_64
name-version(大版本.小版本.修订版)-制作者的修订次数.应用系统.架构
noarch 不区分架构
架构
	x86_64
	Amd64
	i386,i486,i586,i686
	ppc(powerpc)
```

rpm 卸载包

```shell
rpm -e Package 卸载
```

## yum 参考的配置文件

位置:/etc/yum.repos.d/

后缀：repo

```shell
[epel] #名字                                                                                                           
name=Extra Packages for Enterprise Linux 7 - $basearch #描述信息
baseurl=http://mirrors.aliyun.com/epel/7/$basearch #仓库的地址 可以是http:// https:// ftp:// file://(本地)
failovermethod=priority # 设置访问规则
enabled=1  #是否禁用 0表示禁用 1表示启用
gpgcheck=0  # 要不要检查key，1表示检查 0表示不检查
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 
$release 系统版本
$basearch 架构
```

yum 选项

-y yes

-q 静默模式

## yum源的url

- 阿里云
- 网易
- 华为云
- 搜狐
- 腾讯云 <https://mirrors.cloud.tencent.com/>
- 各大高校



## 编译

- 优点：可以自定义功能
- 缺点：安装比较耗时



```shell
yum install zlib-devel
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
tar xf Python-3.6.8.tar.xz
cd Python-3.6.8
./configure --prefix=/opt/python36  检查环节预处理
make 释放makefile文件
make install 安装
```

错误整理

```shell
configure: error: in `/root/test/Python-3.6.8':
configure: error: no acceptable C compiler found in $PATH
yum install gcc
```

添加环节变量

```shell
vim /etc/profile.d/python.sh
PATH=$PATH:/opt/python36/bin

```

