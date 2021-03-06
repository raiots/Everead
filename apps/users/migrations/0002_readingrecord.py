# Generated by Django 4.0.4 on 2022-06-27 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('read_process', models.IntegerField(default=0, verbose_name='阅读进度')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='书籍')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.chapter', verbose_name='章节')),
                ('ebook', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.ebook', verbose_name='书源')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='读者')),
            ],
        ),
    ]
