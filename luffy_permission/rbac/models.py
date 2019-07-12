from django.db import models


class Permission(models.Model):
    """权限表"""
    url = models.CharField('url地址', max_length=100)
    title = models.CharField('标题', max_length=32)
    is_menu = models.BooleanField(default=False, verbose_name='是否是菜单')
    icon = models.CharField('图标', max_length=50)

    def __str__(self):
        return self.title


class Role(models.Model):
    """角色表"""
    name = models.CharField('角色名称', max_length=32)
    permissions = models.ManyToManyField('Permission', verbose_name='角色所拥有的权限', blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    """用户表"""
    username = models.CharField('用户名', max_length=32)
    password = models.CharField('密码', max_length=32)
    roles = models.ManyToManyField('Role', verbose_name='用户所拥有的角色', blank=True)

    def __str__(self):
        return self.username
