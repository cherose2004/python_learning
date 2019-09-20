import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_practice.settings")
import django

django.setup()

from app01 import models

# 基于对象的查询
mjj = models.Author.objects.get(pk=1)
# print(mjj.books)  #  ——》  关系管理对象
# print(mjj.books.all())

# book_obj = models.Book.objects.filter(title='桃花侠大战菊花怪').first()
# 不指定related_name
# print(book_obj.author_set)  #  ——》  关系管理对象
# print(book_obj.author_set.all())
# related_name='authors'
# print(book_obj.authors)  #  ——》  关系管理对象
# print(book_obj.authors.all())

# ret  =  models.Author.objects.filter(books__title='菊花怪大战MJJ')
# print(ret)

# 不指定related_name
# ret = models.Book.objects.filter(author__name='MJJ')
# related_name='authors'
# ret = models.Book.objects.filter(authors__name='MJJ')
# related_query_name='xxx'
# ret = models.Book.objects.filter(xxx__name='MJJ')
# print(ret)


# 关系管理对象的方法

mjj = models.Author.objects.get(pk=1)


# all()  所关联的所有的对象

# print(mjj.books.all())
# set  设置多对多的关系    [id,id]    [ 对象，对象 ]
# mjj.books.set([1,2])
# mjj.books.set(models.Book.objects.filter(pk__in=[1,2,3]))


# add  添加多对多的关系   (id,id)   (对象，对象)
# mjj.books.add(4,5)
# mjj.books.add(*models.Book.objects.filter(pk__in=[4,5]))

# remove 删除多对多的关系  (id,id)   (对象，对象)
# mjj.books.remove(4,5)
# mjj.books.remove(*models.Book.objects.filter(pk__in=[4,5]))

# clear()   清除所有的多对多关系
# mjj.books.clear()

# create()
# obj = mjj.books.create(title='跟MJJ学前端',pub_id=1)
# print(obj)
# book__obj = models.Book.objects.get(pk=1)
#
# obj = book__obj.authors.create(name='taibai')
# print(obj)



