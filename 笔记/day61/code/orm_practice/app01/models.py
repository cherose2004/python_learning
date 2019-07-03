from django.db import models


class MyCharField(models.Field):
    """
    自定义的char类型的字段类
    """

    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为char，长度为max_length指定的值
        """
        return 'char(%s)' % self.max_length


class Person(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField('姓名', max_length=32, db_column='username', unique=True,
                            help_text='不要写乳名')  # name varchar(32)
    age = models.IntegerField(default=18, verbose_name='年纪', editable=False)
    birth = models.DateTimeField(auto_now=True)
    phone = MyCharField(max_length=11, blank=True, null=True)  # 数据库可以为null
    gender = models.BooleanField('性别', choices=((0, '女'), (1, '男')))

    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)

    class Meta:
        db_table = "person"  # 表名
        # 排序
        # ordering = ('age','-pk')

        verbose_name = '个人信息'

        verbose_name_plural = '个人信息'

        index_together = [
            ("name", "age"),  # 应为两个存在的字段
        ]
        #
        unique_together = (("name", "age"),)  # 应为两个存在的字段


class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey(Publisher, related_name='books',related_query_name='xxx',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
