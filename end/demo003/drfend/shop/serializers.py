# ProjectName:Ldemo003
# FileName:serializers
# author:asus
# datetime:2020/2/26 15:41
# software: PyCharm
from rest_framework import serializers
from .models import *


class CategorySerizlizer(serializers.ModelSerializer):
    goods = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ('name', 'goods')


class GoodSerizlizer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        fields = ('name', 'docs', 'price', 'category')
