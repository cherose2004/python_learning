# find

格式： find [OPTION] .... [查找路径] [查找条件] [处理动作]

查找路径：可以指定具体的路径，默认是当前路径

查找条件：用来指定文件查找的标准，可以是文件名、大小、权限、类型等等

处理动作：对符合条件的文件进行的操作，默认是直接输出到屏幕上

## 查找条件

### 按照名称来搜索：

- name ：

  ```SHELL
  find -name a 完全匹配
  find -name "a*" 所有的以a开头的文件或者文件夹
  find -name "a?" 所有以a开头后面为一个字母的文件或者文件夹
  find -name "a[ab]" 以a开头后面是a或者b的文件或者文件夹
  
  ```

- iname 忽略大小写

  ```SHELL
  find -iname a
  ```

### 按照搜索层级

- -maxdepth level 指定最大的搜索层数，指定的目录为第一层

  ```SHELL
  find -maxdepth 2 -name a
  ```

- -mindepth level 指定最小的搜索层数

  ```SHELL
  find -mindepth 2 -name a
  ```

### 按照文件的类型来查找

- -type type
  - f 文件
  - d 目录
  - l 链接
  - s socket套接字
  - b 块设备
  - c 字符设备文件
  - p 管道文件

```SHELL
find -type f -name a 搜索文件
find -type d -name a 搜索目录
find -type l -name a 搜索软链接
```

### 空文件和空目录

- -empty

  ```SHELL
  find -empty
  find -empty -type d
  ```

### 根据属组，属主来搜索

- -user username 查找属主是username的文件或者文件夹
- -group groupname 查找属组是groupname的文件或者文件夹
- -uid uid 查找uid为uid的文件或者文件夹
- -gid gid 查找gid为gid的文件或者文件夹
- -nouser 查找没有属主的文件或者文件夹
- -nogroup 查找没有属组的文件或者文件夹

```shell
find -user jiangyi
chmod :xiaofeng jiangyi
chown :xiaofeng jiangy
find -group xiaofenf
find -group xiaofeng
find -uid 1000 
find -gid 1000 
find -gid 1001
find  -nouser
find -nogroup 
```

### 组合条件

- 与 -a
- 或 -o
- 非 -not !
- 摩根定律
  - （非A）或(非B)=非（A且B）
  - （非A）且（非B）=非（A或B）

```SHELL
find -not -user wupeiqi -a -not -user xiaofeng -ls|wc -l
find -not \( -user wupeiqi -o -user xiaofeng \) -ls|wc -l
```

### 排除目录

- -path

```SHELL
find /etc/ -path /etc/ssh -name *_config
```

### 文件大小来搜索

- -size[+|-] unit 常用单位：k，M，G，c(byte)
  - #unit：(#-1,#] 不包括#-1，但是包括#
  - -#：[0,#-1]，从0到#-1
  - +#：(#,......) 不包括#

###  文件时间戳

- 以“天"为单位
  - atime：[+|-] day
    - time [#,#+1）包括#，但是不包括#+1
    - +time：[#+1,.....]
    - -time:[0,#)
  - mtime
  - ctime
- 以“分钟”为单位
  - -amin
  - -mmin
  - -cmin

### 根据权限来搜索

- -perm 权限

```SHELL
find -perm 644  -ls
find -perm 777  -ls
```

## 处理动作

- -print 把搜索到的结果直接打印到屏幕上，默认的
- -ls 相当于执行`ls -l` 命令
- -delete 删除查找的文件
- -fls filename 将查找结果写入文件中
- -ok command {} \；对查找的文件执行command命令，但是每一次都需要用户确认
- -exec command {} \; 对查找到的文件执行command命令，不需要用户确认
  - {} 表示查找到的文件
  - find 传递的时候 是一次性传递的

# xargs

- 由于好多的命令不支持管道，但是工作有需要用到，这个时候xargs就可以派上用场
- xargs 把一个命令的输出结果，一个一个的传递给后面要执行的命令
- 有些命令不支持太多的字符，也可以使用xargs来传递

```shell
[root@localhost d]#echo a{1..1000000}|xargs touch
[root@localhost d]#rm a{1..1000000}
-bash: /usr/bin/rm: Argument list too long
[root@localhost d]#ls a*|xargs rm -f 
-bash: /usr/bin/ls: Argument list too long
[root@localhost d]#ls |xargs rm -f 
```

一般情况下 find|xargs command

# grep

三剑客

- grep
- sed
- awk

grep：全局用正则表达式搜索，并且打印符合条件的行

grep [option] .... pattern [file]

## 参数

- --color=auto 将匹配到的文本添加颜色显示
- -v 取反，显示没有匹配到
- -i 忽略大小写
- -n 显示匹配到的行的行号
- -c 只显示匹配到的行的个数
- -o 只显示匹配到的字符
- -q 静默模式，不输出东西
- -A # 输出后#行
- -B # 输出前#行
- -C # 前后各输出#行
- -e 表示或者
- -E 扩展正则表达式
- -r 递归查找

```SHELL
 grep 'root' passwd 
 grep -v "root" passwd 
 grep "root" passwd 
 grep -i "root" passwd 
 grep -n "root" passwd 
 grep -ni "root" passwd 
 grep -ci "root" passwd 
 grep -i "root" passwd 
 grep -o "root" passwd 
 grep -oi "root" passwd 
 grep -q "root" passwd 
 grep -q "qwertyuip;qwertyuo" passwd 
 echo $?
 grep -q "root" passwd 
 echo $?
 grep -nA 2 "root" passwd 
 grep -nB 2 "root" passwd 
 grep -nC 2 "root" passwd 
 grep -e "root" -e "mail" passwd 
 grep -r root /etc/ 
```

## 正则表达式

- 字符匹配
  - . 匹配任意单个字符
  - [abc] 匹配执行范围内的任意单个字符  [0-9]
  - [^abc] 取反
  - [:alnum:] 数字大小写 [a-zA-Z0-9] 
  - [:alpha:] 大小写字母 [a-zA-z]
  - [:lower:] 小写字母 [a-z]
  - [:upper:] 大写字母 [A-Z]
  - [:digit:] 数字 [0-9]
  - [:punct:] 标点符号
- 匹配次数
  - \* 0次或者多次，是贪婪匹配
  - \？0次或者一次
  - \\+ 最少一次
  - \\{n\\} 匹配n次
  - \\{m,n\\} 最少m次，最多n次
  - \\{,n\\} 最多n次
  - \\{m,\\} 最少m次
- 位置锚定
  - ^ 行首锚定
  - $ 结尾
  - ^$ 空行
- 向后引用
  - \1:表示前面第一个括号内匹配之后产生的字符，在\1的位置要在出现一次
  - \2:

## egrep

egrep =grep -E

支持扩展正则表达式，与标准增长表达式的区别就是不需要转义

## 压缩

## gzip

Usage: gzip [OPTION]... [FILE]...

```SHELL
gzip passwd 压缩文件 默认会删除文件
gunzip pass.gz 解压文件，默认也会删除文件
gzip -d passwd.gz 解压文件
-c 保留原来的文件
gzip -c passwd > passwd.gz 压缩
gzip -c -d passwd.gz > passwd 解压
-# 1-9 指定压缩比，值越大压缩比例越大 默认是9
zcat 查看压缩包内的文件
zcat passwd.gz > passwd
```

## bzip2

```SHELL
-k 保留原文件
-d 解压
bunzip2 解压
-# 1-9 默认的是9
bzcat 查看压缩包的文件
```

## xz

```shell
-k 保留源文件
-d 解压
unxz 解压
-# 1-9 默认的是9
xzcat 查看压缩包内的文件
```

## tar

```shell
tar cvf a.tar b c
c  创建
v 显示过程
f 指定文件
r 追加
x 解压
-C 指定解压位置
j 使用bzip2来压缩
z 使用gzip来压缩
J 使用xz来压缩
--exclude 排除
tar cvf a.tar b c
tar -r -f a.tar d
tar xf a.tar -C /opt
tar jcvf a.tar.bz b c d
tar zcvf a.tar.gz b c d
tar Jcvf a.tar.xz b c d

tar zcf etc.tar.gz --exclude=/etc/yum.repos.d --exclude=yum.conf /etc/
```

## 分卷压缩

```shell
split -b size file -d tarfile 
-b  指定每一个分卷的大小
-d 指定数字 默认是字母
-a 指定后缀个数
合并：
cat tarfile* > file.tar.gz
dd if=/dev/zero of=b bs=10M count=2
split -b 5M b b.tar.gz
split -b 5M b -d  b.tar.gz
split -b 5M b -d -a 3 b.tar.gz
```

