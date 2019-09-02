## 命令补全

tab键

内部命令：

外部命令：shell 会根据环境变量从左至右依次查找，找到第一个匹配的则返回

- 如果说给定的字符串只能搜索到一个的话，则直接显示
- 如果给定的字符串搜索到多个的话，则需要按两次tab键

目录补全

- 把用户给定的字符串当做路径的开始部分，来搜索
  - 如果只搜索到一个，则直接显示，直接一个tab
  - 如果说搜索到多个的话，列出一个列表，让用户自行选择，需要按两次tab键来获取列表

## echo 回显

输入什么就输出什么，并且加入了一个换行符

## 获取环境变量

```SHELL
[root@localhost ~]#echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
```

## 命令历史

- 可以通过键盘上的箭头来查找之前执行过的命令

- 通过history来获取之前执行过的命令记录

- 执行刚才执行过的命令

  - 键盘上的向上箭头
  - !!
  - !-1
  - ctrl+p

- 使用!:0来执行上一条命令（去掉参数）

- !# 来执行第多少条命令

  ```SHELL
  [root@localhost ~]#!123
  which cp
  alias cp='cp -i'
  	/usr/bin/cp
  ```

- !string 直接查找最近的一条包含string的命令

- ctrl+r 搜索之前执行过的命令

- ctrl+g来退出搜索

- 调用上一个命令的参数

  - esc .

- history 的命令历史

  ```shell
  history # 显示最后的#条命令
  history -c 清空命令记录
  ```

- 当用户登录系统之后，会读取家目录下的.bash_history文件

- 正常退出，会将之前执行过的命令写入到文件中

## 快捷键

ctrl+l 清屏，相当于clear

ctrl+s 锁定屏幕

ctrl+q 解开锁定

ctrl+c 总之命令

ctrl+a 移动到命令的行首 相当于home

ctrl+e 移动到行尾，相当于end

ctrl+xx 光标在命令行首和光标之间来回移动

ctrl +k  删除光标到结尾位置的字符

ctrl+u 删除光标到行首的字符

alt+r 删除正行

需要注意，alt会跟别的快捷键冲突

## 帮助信息

- 内部命令
  - help command
  - man bash
- 外部命令
  - command --help
  - command -h
  - man command     q退出
  - 官方文档

```shell
Usage: date [OPTION]... [+FORMAT]
  or:  date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]
  [] 代表可选
  ... 表示一个列表
  [-u|--utc|--universal] 任选其中一个
  -lh 代表-l -h
  date 052805271980 设置时间
ntpdate time.windows.com  自动与时间服务器同步时间
```



## man

箭头来控制输出

回车输出下一行

空格切换到下一屏

章节

1 用户的命令

2 系统的调用

3 c库的调用

4 设备文件或者特殊文件

5 配置文件

6 游戏

7 杂项

8 管理类的命令

9 linux内核API

## 目录结构

- 目录结构是一个倒置的树
- 目录从“/”开始
- 目录严格区分大小写
- 隐藏文件以.开头
- 路径的分隔符是/

## 文件命名规范

- 文件名最长为255个字符
- 包括路径在内最长4095个字符
- 除了/和NULL以外，其他的字符都生效
- 名称大小写敏感

## 颜色的表示

- 蓝色 表示目录
- 绿色 表示可执行文件
- 红色 表示压缩文件
- 蓝绿色 链接文件
- 白色  普通的文件
- 灰色  其他文件

## 文件系统结构

- /boot 存放系统的引导文件，内核文件、引导的加载器放在该目录
- /bin 所有的用户都可以使用的一些基本命令
- /sbin 管理员可以使用的命令，管理类命令
- /lib 基本的一些库文件（windows 是.dll linux是.so）
- /lib64 专门用于64位操作系统的一些辅助库文件
- /etc 配置文件目录
- /home/Username 普通用户的家目录
- /root 超级管理员的家目录
- /media 便携式移动设备挂载点
- /opt 第三方的安装程序
- /srv 系统上允许的服务用到的数据
- /tmp 存放临时文件的目录
- /usr 存放安装程序
- /var 存放经常变化的数据，比如日志
- /proc 用来存放内核和进程相关的虚拟文件
- /dev 用来存放设备的
- /mnt 临时文件挂载
- /run 服务或者系统启动以后生成的文件
- /sys 存放的是硬件设备相关的虚拟文件

## 程序组成部分

- 二进制
  - /bin
  - /sbin
  - /usr/bin
  - /usr/sbin
  - /usr/local/bin
  - /usr/local/sbin
- 库文件
  - /lib
  - /lib64
  - /usr/lib
  - /usr/lin64
  - /user/local/lib
  - /usr/local/lib64
- 配置文件
  - /etc
  - /etc/directory
  - /usr/local/etc
- 帮助文件
  - /usr/share/man
  - /usr/share/doc
  - /usr/local/share/man
  - /usr/local/share/doc

## 相对路径 绝对路径

绝对路径：

	-	从根开始
	-	完整的路径

相对路径：

	-	相对于某个文件或者目录
	-	不是/开始
	-	.. 代表是父级目录
	-	.代表当前路径

## 获取文件名和文件目录

```shell
[root@localhost network-scripts]#basename /etc/sysconfig/network-scripts/ifcfg-ens33
ifcfg-ens33
[root@localhost network-scripts]#dirname /etc/sysconfig/network-scripts/ifcfg-ens33
/etc/sysconfig/network-scripts
```

## cd

change directory 

可以使用相对路径，也可以使用绝对路径

```SHELL
[root@localhost etc]#cd
[root@localhost ~]#
[root@localhost ~]#cd - 可以快速的回到上一次的目录
/etc/sysconfig/network-scripts
[root@localhost network-scripts]#cd -
/root
```

## pwd

print working directory

```shell
[root@localhost etc]#pwd
/etc
[root@localhost etc]#cd sysconfig/network-scripts/
[root@localhost network-scripts]#pwd
/etc/sysconfig/network-scripts
```

## ls

list 列出指定目录的文件或者文件夹

语法：ls [OPTION]... [FILE]...

```SHELL
ls -a  列出所有的文件（包括隐藏文件）
ls -l =ll 使用长格式来显示文件相关信息
ls —R 递归显示
ls -d 显示目录本身
ls -1（数字1） 竖着显示文件
ls -S 根据文件的大小来排序
ls -lSr 升序排序
ls -d */ 显示当前目录下的目录，不能指定目录
ls -h 以人类易读的方式显示
```

## touch 创建空文件修改文件的时间戳

```SHELL
touch 用来修改时间和创建文件
如果文件存在的话，则修改时间
如果不存在，则创建文件
```

## 命令的展开

```SHELL
a{1..10}   命令展开
a{1..10..2} 指定步长
seq 1 10 
seq 1 2 10
```

## 命令引用

```shell
`date`
$(date)
```

## 文件通配符

- \* 代表零个或者多个字符
- ? 代表任意的一个字符
- ~ 代表家目录
- [0-9] 代表数字
- [a-z] 字母，从a-z并且包括A-Y
- [A-Z] 字母，从A-Z 并且包括b-z
- [abcdef] 表示其中的任何一个
- a\[^abcdef] 取反
- [:lower:] 小写字符
- [:upper:] 大写字符
- [:digit:] 数字
- a-zA-Z 所有字母
- [:alpha:] 所有字母
- a-zA-Z0-9 任意字母或者数字
- [:alnum:] 代表所有的字母和数字

## stat 查看文件状态

```shell
  File: ‘aa’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: fd00h/64768d	Inode: 19864315    Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Context: unconfined_u:object_r:admin_home_t:s0
Access: 2019-07-30 11:57:02.279384871 +0800
Modify: 2019-07-30 11:57:02.279384871 +0800
Change: 2019-07-30 11:57:02.279384871 +0800
 Birth: -
访问时间：access      读取文件内容  atime
修改时间：Modify      改变文件的内容 mtime
改变时间：change      改变文件的内容 ctime
```

## 复制文件和文件夹

```shell
Usage: cp [OPTION]... [-T] SOURCE（源文件） DEST（目标文件）
  or:  cp [OPTION]... SOURCE... DIRECTORY
  or:  cp [OPTION]... -t DIRECTORY SOURCE...

```

- 如果source是一个文件的话
  - 如果目标不存在，新建一个目标文件，并将数据写入到目标文件里面
  - 如果目标文件存在
    - 如果目标文件是一个目录，直接在目标目标下面新建一个跟源文件同名的文件，并将数据目标文件写入到文件
    - 如果说目标文件是一个文件，直接就覆盖，为了安全起见，建议cp配合-i使用
- 如果源文件是多个文件的话
  - 目标文件如果是文件的话，则直接报错
  - 如果目标文件是一个目录的话，则直接复制进目录
- 如果源文件是目录的话
  - 如果目标不存在，则创建指定的目录，必须-r选项
  - 如果说目录存在
    - 如果目录是一个文件的话，则会报错
    - 如果目标是一个目录的话，则在目录下面创建一个新的同名目录，并把文件复制过去

常用参数

```SHELL
-i 覆盖之前提示
-n 覆盖前不提示
-r 递归复制，复制目录及目录下的所有文件
-f 强制
-v 显示复制过程
-b 在覆盖之前，对源文件做备份
cp  --backup=numbered 1.cfg 2.cfg 覆盖文件，备份文件添加上数字
-p 保留原来的属性
```

## 移动或者重命名

```SHELL
Usage: mv [OPTION]... [-T] SOURCE DEST
  or:  mv [OPTION]... SOURCE... DIRECTORY
  or:  mv [OPTION]... -t DIRECTORY SOURCE...
-i  交互式
-f  强制
-b  覆盖前做备份
-v 显示进度
```

## 删除

```SHELL
rm [OPTION]... FILE...
-i 交互式
-f 强制删除
-r 递归删除
rm -rf /* 慎用
rm -rf /* 慎用
rm -rf /* 慎用
cd /
rm -rf *
```

