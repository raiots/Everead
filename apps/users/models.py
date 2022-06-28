from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from apps.books.models import Book, eBook, Chapter


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, verbose_name='用户名')
    nickname = models.CharField(max_length=150, verbose_name='昵称')
    email = models.EmailField(max_length=150, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.nickname


class MyGroup(Group):
    class Meta:
        verbose_name = '权限组'
        verbose_name_plural = '权限组'


class ReadingRecord(models.Model):
    reader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='读者')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='书籍')
    ebook = models.ForeignKey(eBook, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='书源')
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='章节')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    read_process = models.IntegerField(default=0, verbose_name='阅读进度')
