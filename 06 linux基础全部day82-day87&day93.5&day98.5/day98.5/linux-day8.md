Docker

cgroup

namespace

IAAS

PAAS

SAAS

centos7 docker

centos6 docker-io

docker-ce 开源社区

docker-ee 收费版本

# 安装

1.卸载原来的docker

```SHELL
yum remove docker
```

2.下载阿里云的docker仓库

```SHELL
wget -O /etc/yum.repos.d/docker-ce.repo  https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo 
```

3. 安装

   ```shell
   yum install docker-ce -y
   ```

# 镜像

类似于安装系统时候需要的iso镜像文件

# 容器

启动之后的镜像



# 仓库

存放镜像

可以用公用的

可以有私有的

```python
class myclass():
    def __init__():
        pass
    
m=myclass()
```

# 测试docker是否安装正常

```shell
docker run hello-world

run 运行
hello-world 镜像名称
```

# 搜索镜像

```shell
NAME(名字)                             DESCRIPTION(描述信息)                                     STARS(点赞数)              OFFICIAL(是否为官方)            AUTOMATED
mysql                             MySQL is a widely used, open-source relation…   8499                [OK]                
mariadb                           MariaDB is a community-developed fork of MyS…   2942                [OK]                

```

# 下载镜像

```shell
docker pull 镜像名称

```

# 运行容器

- 如果本地没有此镜像,则会取docker  hub 下载
- 如果有的话,则直接根据参数运行

```SHELL
docker run
-d  后台启动
docker run --name redis-test -d redis 起名字
-it
-i 交互式操作
t 终端
--rm 容器退出,并把容器删掉
```



# 查看本地镜像

```SHELL
docker images
-q 只显示id
```

# 查看启动的容器

```shell
docker ps
-a  显示启动过的所有的容器

```

# 删除镜像

```SHELL
docker rmi 删除镜像
默认情况下不能删除启动过容器的镜像
-f 强制删掉
```

# 删除容器

```shell
docker rm id|name 删除容器
默认不能删除启动中的容器
-f 强制删除

```

# 退出容器不关闭容器

```shell
ctrl+p,q
```

# 进入正在启动中的容器

```shell
docker exec -it id|name bash
bash 是进入容器后执行的命令

```

# 查看容器的log日志

```shell
docker logs id|name
-f 查看实时日志输出

```

# 导出镜像

```shell
docker save -o name imagename|id
docker save id|imagesname > centos.tar.gz
```

# 导入镜像

```shell
docker load -i centos.tar.gz
docker load < centos.tar.gz 
```

# 提交

```shell
docker commit -m "message" 运行中的容器id
```

# 修改镜像名称

```shell
docker tag 原来名称 新名称
如果不存在tag,则在原来的镜像基础上加上tag信息,如果存在原来的tag信息,则会复制一份
```


# 删除所有的关闭状态下的容器

```SHELL
docker container prune
```

# 数据卷

将宿主机的文件挂载到容器里面

```shell
-v 宿主机目录:容器目录
docker run -it -v /opt/myetc:/etc centos bash
```

# 端口映射

```SHELL
docker run -d -P redis 端口是随机产生
docker run -d -p 宿主机上的端口:容器内的端口 redis 指定端口
```

# 查看容器的资源占用率

```shell
docker stats 容器id|name
```

docker info 查看docker信息

docker inspect 查看镜像信息

# dockerfile

```SHELL
FROM mycentos  指定基础镜像
RUN yum install -y wget 执行命令
RUN mkdir /mydata
COPY a.txt /mydata 将本地文件复制到镜像里面
ADD etc.tar.gz /mydata  将本地文件复制到进项内,如果是压缩包,则自动解压
WORKDIR /mydata 指定工作目录,exec 进入时候默认的目录
ENV 设置变量
VOLUME 设置数据卷
EXPOSE 5900 设置端口
CMD ["nginx", "-g", "daemon off;"] 执行命令
```

copy 和add的区别

add 是自动解压

CMD只能有一个,RUN可以有多个

# 本地私有仓库

```shell
docker run -d -p 5000:5000 -v /opt/register:/var/lib/registry registry
docker tag redis 127.0.0.1:5000/redis 修改名称
docker push 127.0.0.1:5000/redis  上传到仓库
curl  127.0.0.1:5000/v2/_catalog 查看结果
```

要修改文件/etc/docker/daemon.json

```SHELL
{
	# 配置加速
    "registry-mirrors": [
        "https://1nj0zren.mirror.aliyuncs.com",
        "https://docker.mirrors.ustc.edu.cn",
        "http://f1361db2.m.daocloud.io",
        "https://registry.docker-cn.com"
    ],
    # 本地仓库地址
     "insecure-registries": [
    "192.168.182.130:5000"
  ]
}

```

# docker-compose

排版工具:

swam

docker-compose



yml 可以用来做配置文件

cfg

ini

xml

json

后缀名: yml yaml

数据类型:

string

int

列表: [ ] \-

字典

key:value

salt

ansible

docker-compose

k8s

```SHELL
version: '3'
services:
   web: 
     build: 
        context: . 在哪
        dockerfile: dockerfile文件
     ports:
     - "3000:3000"
   redis:
     image: "redis"

```

```shell
from flask import Flask
from redis import Redis

app=Flask(__name__)
redis=Redis(host="redis",port=6379)

@app.route("/")
def index():
    count= redis.incr("hits")
    return "该页面被访问了{}次".format(count)

if __name__=="__main__":
    app.run(port=3000,host="0.0.0.0")

```



build 重新构建容器

ps 查看运行中的容器

images  查看镜像

rm 删除停止容器

```shell
version: '3' #版本
services:
   web: 
     build: . # dockerfile文件叫Dockerfile
     ports:
     - "3000:3000"
   redis:
     image: "redis"
```

```shell
version: "3" 
services:

  redis:
    image: redis:alpine
    ports:
      - "6379"
    networks:
      - frontend

  db:
    image: postgres:9.4
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend

  vote:
    image: dockersamples/examplevotingapp_vote:before
    ports:
      - 5000:80
    networks:
      - frontend
    depends_on:  # 先谁启动
      - redis
      - db

```

dockerfile 部署crm

```shell
FROM python:3.6-alpine3.9  # 基础镜像
RUN mkdir /data   # 执行命令
COPY requirements.txt /data # 复制文件
COPY mycrm /data  #复制目录的时候,,默认情况下是复制目录下的所有文件,如果要复制整个目录,则需要在后面加上目录名称
WORKDIR /data # 指定工作目录
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple #安装python第三方的包
EXPOSE 8080 # 启动时候的端口,必须的
CMD python manage.py runserver 0.0.0.0:8080 #启动django

```



