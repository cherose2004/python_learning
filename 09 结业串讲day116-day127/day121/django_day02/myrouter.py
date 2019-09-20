class Router:
    """
    读写分离

    """

    def db_for_write(self, model, **kwargs):
        return 'db2'

    def db_for_read(self, model, **kwargs):
        return 'default'


import random


class Router:
    """
    一主多从
    """

    def db_for_write(self, model, **kwargs):
        return 'db1'

    def db_for_read(self, model, **kwargs):
        return random.choices['db2', 'db3', 'db4']


class Router:
    """
    分库分表

    app01  model   db1
    app02  model   db2
    """

    def db_for_write(self, model, **kwargs):
        app_name = model._meta.app_label
        if app_name == 'app01':
            return 'db1'
        elif app_name == 'app02':
            return 'db2'

    def db_for_read(self, model, **kwargs):
        app_name = model._meta.app_label
        if app_name == 'app01':
            return 'db1'
        elif app_name == 'app02':
            return 'db2'
