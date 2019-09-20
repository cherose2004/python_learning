# -*- coding: utf-8 -*-
# __author__ = "maple"
import importlib
import settings

module_path,class_name = settings.DATA_PATH.rsplit('.',1)

m = importlib.import_module(module_path)
cls = getattr(m,class_name)
obj = cls()
obj.f1()