from django.db import models
# from apps.users.models import User


# Create your models here.
def book_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'books/{0}/{1}'.format(instance.title, filename)


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    cover = models.ImageField(upload_to=book_directory_path, blank=True)
    cate = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class eBook(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    ebook_version = models.IntegerField(default=0, unique=True)
    # uploader = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    ebook_file = models.FileField(upload_to='books/txt/')
    chapter_num = models.IntegerField(default=0)
    total_lines = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)


class Chapter(models.Model):
    ebook = models.ForeignKey(eBook, on_delete=models.CASCADE)
    chapter_index = models.IntegerField(default=0, unique=True)
    title = models.CharField(max_length=50)
    start_line = models.IntegerField(default=0, unique=True)
    slice_file = models.FilePathField(path='books/txt/')
