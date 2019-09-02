昨日补充

```SHELL
ls -ltu 按照atime时间排序
cp -n  不覆盖
```

## mkdir

```shell
mkdir s21
mkdir s21-{3..10}
mkdir -p a/b/c/d
mkdir -pv {s13,s14}/{ss11,ss12}/{sss11,sss12} 
-p 递归创建
-v 显示创建过程
```

## tree

```shell
yum install -y tree
tree name
-L 控制显示的层数
-b 只显示目录
```

## 文件类型

- \- 表示文件
- d表示目录
- l 表示链接
- b 块设备
- c 字符设备
- s 表示socket套接字

## rmdir 

只能删除空目录

```SHELL
mkdir -p s15/s16/s17/s18
rmdir -p s15/s16/s17/s18
```

## 链接

- 硬链接
  - ln 源文件 目标文件
  - 源文件发生改变，目标会发生改变
  - 将硬盘的引用次数+1
  - 删除
    - 将磁盘上的引用次数-1
    - 源文件删除对目标不会受影响
  - 不能对目录做硬链接
  - 不能跨越分区
- 软链接
  - 相当于windows的快捷方式
  - ln -s 可以生成软链接
  - 链接大小就是制定的源文件的字符数
  - 源文件发生改变，目标会发生改变
  - 删除
    - 源文件删除目标会收影响
  - 可以对目录做软链接
  - 可以跨域分区



## 文件权限

```shell
drwxr-xr-x. 4                          root root 30 Jul 31 08:55 s12
	权限     在磁盘上的引用次数（硬链接）    属主  属组 大小  atime      文件名 
```

## 输入 输出

### 输入

标准输入：接收来自键盘的输入 stdin 0

### 输出

标准输出：默认输出到终端  stdout 1

错误输出：默认输出到终端 stderr  2

## i/o重定向

把输出和错误信息重定向到文件或者别的地方

\> 覆盖

- \> 把stdout的数据重定向到文件里面
- 2> 把stderr信息重定向到文件里面
- &> 把所有的输出都同事重定向到文件

\>> 追加

- \>> 把标准的数据追加到文件中
- 2>> 把错误输出追加到文件中
- &>> 把所有的输出都同时追加到文件里面

## 分文件输出

```SHELL
ls b bbbbb > info.log 2> error.log
```

## 合并输出

- &> 
- &>>
- command > info.log 2>&1
- command > info.log 2>>&1
- /dev/null 无线接收的无底洞
- （）多个合并

## tr 替换或者删除字符

```SHELL
tr 'a-z' 'A-Z' </etc/issue
[root@localhost jiangyi]#tr ab 12
ab
12
[root@localhost jiangyi]#tr abc 12  如果后面的位数不足的话，则用最后一位补齐
abc
122
ab
12
tr -d abc < issue > issue2 从定向不能为原来的文件，如果说为原来的文件，则文件情况
-t 用来截断
[root@localhost jiangyi]#tr -t abcd 12
abcd
12cd
cd
cd
-s 压缩 去重
[root@localhost jiangyi]#tr -s abc
abc
abc
aaabbbccccccccccccccccccccccccccccc
abc
-c 取反
[root@localhost jiangyi]#tr -sc abc
aaaaaaaaaaaaaabbbbbbbbbbbbbbbcccccccccccccc
aaaaaaaaaaaaaabbbbbbbbbbbbbbbcccccccccccccc
aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbcccccccccccccccccdddddddddddddeeeeeeeeeeeeffffffffffffff
aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbcccccccccccccccccdef
aaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccc1111111111111111222222222222333333333333
aaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccc123
[root@localhost jiangyi]#tr -dc abc
aaaaaaaaaaaaabbbbbbbbbbbbccccccccccccccccccdddddddddddddddwqweqweqwqeqwqwqwq
wqqqqqqqqqqqqqqqqqqqqqqqqq
ctrl+d结束
[root@localhost jiangyi]#tr -dc "abc\n"
adsada
aaa
sadasdcxzczx
aacc
asdadwq
aa
[root@localhost jiangyi]#seq 1 10 >f1
[root@localhost jiangyi]#tr -d "\n" <f1
[root@localhost jiangyi]tr "\n" " "<f1
[root@localhost jiangyi] tr " " "\n" <f2

```

## 禁止覆盖

```shell
set -C 禁止覆盖
set +C 允许覆盖
```



## 多行输入

```shell
[root@localhost jiangyi]#cat >f1 <<EOF
> 1
> 2
> 3
> 4
> 5
> 6
> 7
> 
> 8
> 9
> EOF
[root@localhost jiangyi]# cat > f4
asdas
sad
asd
ctrl+d结束 ctrl+c也可以
两者区别
第一种方式输出结束，文件才会产生
第二方式，回车一次就会写入文件
EOF 约定俗成
```

## 管道

使用“|”来连接多个命令

命令1|命令2|命令3|。。。。

- 将命令的stdout发送给命令2的stdin，将命令2的stdout命令发送给命令3的stdin。。。。。
- stderr默认是不能通过管道传递

```SHELL
[root@localhost jiangyi]#ls /dadadasda|tr -s "a-z" "A-Z"
ls: cannot access /dadadasda: No such file or directory
[root@localhost jiangyi]#ls|tr "a-z" "A-Z"

```

## 查看当前的登录的用户信息

```SHELL
whoami  获取登录的用户
[jiangyi@localhost ~]$who am i
jiangyi（用户）  pts/4（登录的终端）        2019-07-31 08:27（登录的时间） (192.168.182.1（登录ip地址）)
w 可以查看当前登录的所有用户执行的命令

```



# 文件权限

## chown change owner

```shell
Usage: chown [OPTION]... [OWNER][:[GROUP]] FILE...
  or:  chown [OPTION]... --reference=RFILE FILE...
chown jiangyi d  修改属主
chown jiangyi:jiangyi d 修改属主和属组
chown root.root d
chown :jangyi d 只修改属组信息
chown -R jiangyi a 递归修改目录下的所有文件
chown --reference=b f3 指定源文件
```

### chgrp

```shell
chgrp jiangyi b
chgrp --reference=b f3 指定源文件
```

## 权限

rwxr-xr-x 

三位为一组

属主   属组     其他

u         g          o

r read 可以读这个文件或者文件夹

w write 可以对这个文件或者文件夹有写的权限

x excut 执行的权限

文件

- r 可以查看
- w 可以修改内容
- x 可以直接执行

目录：

- r 可以使用ls查看 可以cd进去
- w  可以在其中创建文件或者目录，可以删除目录中的文件或者是文件夹
- x 可以cd，如果没有x权限的话，w权限不会生效，r权限可以查看有哪些文件

## chmod

- 可以直接用+-来操作

  - 可以用[u|g|o]+ - = r w x
  - 可以什么都不写，表示全部 +-

- 还可以用数字表示

  \---

  r--    100 4

  -w- 010   2

  --x 001   1

  r:4

  w:2

  x:1

  r-xr-x--- 

- 建议：

  - 不要给文件或者文件夹设置成777权限
  - 不要给文件或者文件夹设置成777权限
  - 不要给文件或者文件夹设置成777权限

## 特殊权限

```shell
chattr +i 不能删除、改名、不能修改内容
chattr +a 只能追加，不能删除，不能改名
lsattr 查看属性
```

# 文本处理工具

## cat

```shell
Usage: cat [OPTION]... [FILE]...
-E 显示行的结束符号$
-n 显示每一行的行号
-b 给非空行编号
-s 折叠空行为一行
```

## tac 倒叙显示文件内容

## less 分屏显示

- 可以分屏显示
- 空格一屏  回车一行
- /来搜索
- n 向下搜索 N 向上搜索
- q来退出

## more

- 可以分屏显示
- 空格一屏 回车一行
- -d 显示翻页和推出信息
- 输出自己退出

## head  显示前多少行 默认是10行

- -# 显示前多少行的数据

## tail 显示后面多少行 默认是后10行

- ​	-# 显示后多少行的数据
-  -f 追踪显示文件新加入的内容，常用于日志的跟踪
- tailf 相当于tail -f 命令，

## cut 抽取文件

```SHELL
-d 用来指定切割符号
-f 执行显示哪一个数据
# 显示指定的数据
#，#，#，# 离散数据
#-# 连续数据
cut -d: -f3 passwd 
cut -d: -f1,3-7 passwd 
cut -d: -f3,4,5,6 passwd
cut -d: -f3-6 passwd 
-c 按照字符切割
cut -c2-5 passwd
```

## paste 合并文件

```shell
-d 用来指定合并的符号，默认的是tab
-s 把所有的行合并成一行显示
```

# 分析文本的工具

## wc word count

```SHELL
[root@localhost jiangyi]#wc passwd 
  44   87 2301 passwd
 行数   单词个数  字节数  文件
 -l 统计行的个数
 -w 统计单词的个数
 -c 统计字节的个数
 -m 统计字符的个数
 -L 显示最长一行的长度
```

## sort 排序

```SHELL
默认按照字母
-n 按照数字来排序
-r 按照倒叙来排序
-R 随机排序
sort -t: -nk4 passwd 切割以后在排序
-t 指定切割符号
-k 指定按照第几行排序
```

## uniq 删除重复的行

```SHELL
-c 显示重复出现的次数
-d 只显示重复的行
-u 只显示不重复的行
连续且完全一样的才是重复
ss -tnp|cut -d: -f2|tr -s " "|cut -d" " -f2|sort -n|uniq -c
```

## diff 对比两个文件

```SHELL
[root@localhost jiangyi]#echo "abc" >b
[root@localhost jiangyi]#echo "abcd" >d
[root@localhost jiangyi]#diff b d
1c1
< abc
---
> abcd
[root@localhost jiangyi]#echo "abcde" >b
[root@localhost jiangyi]#diff b d
1c1
< abcde
---
> abcd
[root@localhost jiangyi]#echo "abcde" >> b
[root@localhost jiangyi]#diff b d
1,2c1
< abcde
< abcde
---
> abcd
[root@localhost jiangyi]#echo "abcd" >> b
[root@localhost jiangyi]#diff b d
1,2d0
< abcde
< abcde
```



