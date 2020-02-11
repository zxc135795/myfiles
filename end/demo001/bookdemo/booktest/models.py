from django.db import models


# Create your models here.
# 数据模型


class Book(models.Model):
    """
    book继承了model类
    """
    title = models.CharField(max_length=20)
    price = models.FileField(default=0)
    pub_date = models.DateField(default="1983-06-01")


class Hero(models.Model):
    """
    hero继承
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
