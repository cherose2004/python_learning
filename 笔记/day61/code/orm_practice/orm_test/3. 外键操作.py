import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_practice.settings")
import django

django.setup()

from app01 import models

# 基于对象的查询
# 正向
book_obj = models.Book.objects.get(title='菊花怪大战MJJ')
# print(book_obj.pub)

# 反向
pub_obj = models.Publisher.objects.get(pk=1)
# print(pub_obj.book_set.all())  # 类名小写_set   没有指定related_name
# print(pub_obj.books.all())  #  指定related_name='books'


# 基于字段的查询

ret = models.Book.objects.filter(title='菊花怪大战MJJ')
#  查询老男孩出版的书
ret = models.Book.objects.filter(pub__name='老男孩出版社')

# 查询出版菊花怪大战MJJ的出版社


# related_name='books'
# ret= models.Publisher.objects.filter(books__title='菊花怪大战MJJ')

# 没有指定related_name   类名的小写
# ret= models.Publisher.objects.filter(book__title='菊花怪大战MJJ')

# related_query_name='xxx'

ret= models.Publisher.objects.filter(xxx__title='菊花怪大战MJJ')


print(ret)

