# 模块
    # os 和操作系统打交道的  - 计算文件夹的大小
# import os
# print(os.path.getsize('pack'))
        # 文件
        # 文件夹
        # listdir ，walk
        # 路径
    # sys
        # sys.path    模块搜索路径 一个模块是否能被导入 全看sys.path中是不是有这个模块所在的路径
        # sys.argv    获取命令行的参数  python c://aaa.py  remove 文件路径
        # sys.modules 存储了当前程序中用到的所有模块，反射本文件中的内容
    # datetime
        # now() datetime对象
        # utc() 当前的英国伦敦的时间
        # strftime('%Y-%m-%d %H:%M:%S') 格式化时间
        # strptime('2019-1-1 10:23:23','%Y-%m-%d %H:%M:%S')) 获取到一个datetime对象
        # timedelta(days=140)  时间的加
        # fromtimestamp(时间戳时间)  时间戳转datetime
        # timestamp(datetime对象)  datetime转时间戳
# from datetime import datetime
# dt = datetime.now()
# print(datetime.timestamp(dt))
    # time
        # time() 时间戳时间
        # sleep(n) 让程序在这暂停n秒
    # hashlib  摘要算法模块
        # 密文验证
        # 校验文件的一致性
        # md5
        # sha
# import hashlib
# md5 = hashlib.sha1('盐'.encode())
# md5.update(b'str')
# print(md5.hexdigest())
# 863c5545d295eef3dffe556a141a48b30565c763
        # 序列化 把其他数据类型转换成 str/bytes类型
        # 反序列化 str/bytes类型 转换回去
    # json 所有的语言都支持
        # json格式 ：
            # 1.所有的字符串都是双引号
            # 2.最外层只能是列表或者字典
            # 3.只支持 int float str list dict bool
            # 4.存在字典字典的key只能是str
            # 5.不能连续load多次
    # pickle 只支持python语言
        #  1.几乎所有的数据类型都可以写到文件中
        #  2.支持连续load多次

    # random
    #     randint
import random
# print(random.uniform(1,5))
# print(random.choice([1,2,3,4,5]))   # 验证码 抽奖
# print(random.sample([1,2,3,4],3))   # 一个奖项抽取多个人
    #     choice
    #     sample
    #     shuffle   # 洗牌  算法

    # logging
        # 两种配置方式
            # basicconfig
            # logger对象
    # collections
        # OderedDict
        # namedtuple
        # deque 双端队列
        # defaultDict 默认字典，可以给字典的value设置一个默认值
    # shutil
        # import shutil
        # shutil.make_archive()  压缩文件
        # shutil.unpack_archive() 解压文件
        # shutil.rmtree() 删除目录
        # shutil.move()  重命名 移动文件
    # getpass 在命令行密文显示输入的内容
    # copy.deepcopy
    # importlib
        # importlibimport importlib
        # importlib.import_module('模块名')
        # os = __import__('os')
        # print(os.path.isdir('D:\code\day24\pack'))
        # print(os.path.isfile('D:\code\day24\pack'))
    # functools
        # reduce(add,iterable)

# 面向对象
    # 基础概念
        # 什么是类 : 具有相同方法和属性的一类事物
        # 什么是对象、实例 : 一个拥有具体属性值和动作的具体个体
        # 实例化 ：从一个类 得到一个具体对象的过程
    # 组合
        # 一个类的对象作为另一个类对象的实例变量
            # python是课程类的对象
            # 晶晶是学生类的对象
            # 晶晶.course = python
    # 三大特性
        # 继承
                # 所有的查找名字（调用方法和属性）都是先找自己的，自己没有找父类
                # 如果自己和父类都有，希望自己和父类都调用，super()/指定类名直接调
            # 父类、基类、超类
            # 子类、派生类
            # 单继承 ：字类可以使用父类的方法
            # 多继承
                # 查找顺序
                    # 深度优先
                    # 广度优先
        # 多态
            # 一个类表现出来的多种状态 --> 多个类表现出相似的状态
                # vip_user
                    # 支付
                    # 浏览商品
                # svip_user
                    # 支付
                    # 浏览商品
            # 鸭子类型
                # vip_user  svip_user
                # list 和 tuple
        # 封装
            # 广义的封装 ：类中的成员
            # 狭义的封装 ：私有成员
                # __名字
                # 只能在类的内部使用，既不能在类的外部调用，也不能在子类中使用
                # _类名__名字

# class A:
#     def __func(self):
#         print('A')
#
# class B(A):
#     def func(self):
#         self.__func()
# B()

    # 类成员
        # 类变量
        # 绑定方法
        # 特殊成员
            # 类方法 classmethod
            # 静态方法 staticmethod
            # 属性 property
    # 双下方法/魔术方法/内置方法
        # __str__
        # __new__  构造方法
        # __init__ 初始化方法
        # __call__ 源码中很容易写这个用法
        # __enter__ __exit__  with上下文管理
        # __getitem__
        # __settitem__
        # __delitem__
        # __add__
        # __iter__
        # __dict__

    # 相关内置函数
        # isinstance 对象和类
        # issubclass 类和类
        # type 类型 类 = type(对象)
        # super 遵循mro顺序查找上一个类的

    # 新式类和经典类
        # py2 继承object就是新式类
        #     默认是经典类
        # py3 都是新式类，默认继承object

        # 新式类
            # 继承object
            # 支持super
            # 多继承 广度优先C3算法
            # mro方法
        # 经典类
            # py2中不继承object
            # 没有super语法
            # 多继承 深度优先
            # 没有mro方法