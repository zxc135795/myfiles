from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名称')

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20, verbose_name='商品名')
    price = models.FloatField(default=0, verbose_name='价格')

    docs = models.CharField(max_length=20, verbose_name='商品描述')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='所属分类', related_name='goods')

    def __str__(self):
        return self.name


class GoodImgs(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name='商品图')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='imgs', verbose_name='商品')

    def __str__(self):
        return self.good.name


class User(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name='手机号')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    good = models.ManyToManyField(Good, verbose_name='商品')

    def __str__(self):
        return self.user.username
