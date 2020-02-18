from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name='手机号')
    questions = models.ManyToManyField('Question')


class Question(models.Model):
    title = models.CharField(max_length=50, verbose_name='投票问题')
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Mate:
        # verbose_name = '投票问题'
        verbose_name = '投票问题'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']


class Choices(models.Model):
    content = models.CharField(max_length=50, verbose_name='选项')
    votes = models.PositiveIntegerField(verbose_name='票数')
    create_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices', verbose_name='所属问题')

    def __str__(self):
        return self.content

    class Mate:
        verbose_name = '选项'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
