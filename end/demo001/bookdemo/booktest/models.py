from django.db import models


# Create your models here.
# 数据模型


class Book(models.Model):
    """
    book继承了model类
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")
    author = models.CharField(max_length=20, blank=True)

    def __str__(self):
        # 返回字符串
        return self.title


class Hero(models.Model):
    """
    hero继承
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='heros')

    def __str__(self):
        return self.name


class UserManager(models.Manager):
    def deleteByTelephone(self, tele):
        user = self.get(telephone=tele)
        user.delete()

    def createUser(self, tele):
        user = self.model()
        user.telephone = tele
        user.save()


class User(models.Model):
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')

    objects = UserManager()

    def __str__(self):
        return self.telephone

    class Meta:
        db_table = '用户类'
        ordering = ['id']
        verbose_name = '用户模型'
        verbose_name_plural = '用户模型'
