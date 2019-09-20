import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_practice.settings")
import django

django.setup()

from app01 import models

from django.db import transaction

try:
    with transaction.atomic():
        # 进行一系列的ORM操作

        models.Publisher.objects.create(name='xxxxx')
        models.Publisher.objects.create(name='xxx22')

except Exception as e :
    print(e)