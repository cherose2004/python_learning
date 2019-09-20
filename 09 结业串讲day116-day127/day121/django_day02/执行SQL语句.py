import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_day02.settings")
import django

django.setup()

from app01 import models

# 1. extra

ret = models.Student.objects.all().extra(where=['id > %s'], params=['1'], order_by=['-id'])
# print(ret)
# for i in ret:
#     print(i)


# 2. raw

ret = models.Student.objects.raw('select * from main.app01_classes where id <= 2')
print(ret)
for i in ret:
    print(i.name)

# 3 connection
from django.db import connection, connections

# cursor = connection.cursor()
cursor = connections['db2'].cursor()
cursor.execute("""SELECT * from main.app01_classes where id > %s""", [1])
row = cursor.fetchall()
print(row)
