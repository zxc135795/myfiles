from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET POST PUT PATCh DELETE 等 HTTP 动词操作
    queryset 指明 操作模型

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerizlizer
