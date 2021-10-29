from os import terminal_size
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        verbose_name='제목',
        max_length=80,
    )

    content = models.TextField(
        verbose_name='내용'
    )

    created_at = models.DateTimeField(
        verbose_name='작성일'
    )

    created_by = models.CharField(
        verbose_name='작성자',
        max_length=100
    )

    is_view = models.BooleanField(
        verbose_name='공개 여부',
        default=True
    )


class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)