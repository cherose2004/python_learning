from django.db import models


# rbac

# 简单权限控制
class Permission(models.Model):
    url = models.CharField(max_length=64, verbose_name='权限')


class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='角色')
    permissions = models.ManyToManyField('Permission')


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField('Role')


# 生成一级菜单
class Permission(models.Model):
    url = models.CharField(max_length=64, verbose_name='权限')
    title = models.CharField(max_length=32, verbose_name='标题')
    icon = models.CharField(max_length=32, verbose_name='图标')
    is_menu = models.BooleanField(default=False, verbose_name='是否是菜单')


class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='角色')
    permissions = models.ManyToManyField('Permission')


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField('Role')


# 生成二级菜单
class Menu(models.Model):
    """一级菜单"""
    title = models.CharField(max_length=32, verbose_name='标题')
    icon = models.CharField(max_length=32, verbose_name='标题')


class Permission(models.Model):
    url = models.CharField(max_length=64, verbose_name='权限')
    title = models.CharField(max_length=32, verbose_name='标题')
    menu = models.ForeignKey(Menu, null=True, blank=True)  # menu_id


class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='角色')
    permissions = models.ManyToManyField('Permission')


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField('Role')


#  非菜单权限归属
class Menu(models.Model):
    """一级菜单"""
    title = models.CharField(max_length=32, verbose_name='标题')
    icon = models.CharField(max_length=32, verbose_name='标题')


class Permission(models.Model):
    """
    有parent_id  当前的权限就是子权限
    有menu_id     当前的权限就是父权限  二级菜单
    """
    url = models.CharField(max_length=64, verbose_name='权限')
    title = models.CharField(max_length=32, verbose_name='标题')
    menu = models.ForeignKey(Menu, null=True, blank=True)  # menu_id
    parent = models.ForeignKey('self', null=True, blank=True)  # parent_id


class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='角色')
    permissions = models.ManyToManyField('Permission')


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField('Role')


#  权限控制到按钮级别
class Menu(models.Model):
    """一级菜单"""
    title = models.CharField(max_length=32, verbose_name='标题')
    icon = models.CharField(max_length=32, verbose_name='标题')


class Permission(models.Model):
    """
    有parent_id  当前的权限就是子权限
    有menu_id     当前的权限就是父权限  二级菜单
    """
    url = models.CharField(max_length=64, verbose_name='权限')
    title = models.CharField(max_length=32, verbose_name='标题')
    name = models.CharField(max_length=32, unique=True, verbose_name='URL的别名')
    menu = models.ForeignKey(Menu, null=True, blank=True)  # menu_id
    parent = models.ForeignKey('self', null=True, blank=True)  # parent_id


class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='角色')
    permissions = models.ManyToManyField('Permission')


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField('Role')
