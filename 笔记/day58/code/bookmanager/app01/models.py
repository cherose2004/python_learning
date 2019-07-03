from django.db import models


class Publisher(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    addr = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book',through='AuthorBook',through_fields=['author','book'])  # 不在Author表中生产字段，生产第三张表


class AuthorBook(models.Model):
    author = models.ForeignKey(Author,related_name='a' ,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    tuijian = models.ForeignKey(Author,related_name='b',on_delete=models.CASCADE)

    date = models.DateField()




