from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def categoryList(request):
    if request.method == "GET":
        seria = CategorySerizlizer(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        seria = CategorySerizlizer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:

            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def categoryDetail(request, cid):
    model = get_object_or_404(Category, pk=cid)
    if request.method == "GET":
        seria = CategorySerizlizer(instance=model)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT' or request.method == 'PATCH':
        seria = CategorySerizlizer(instance=model, data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse('没有此项')


@api_view(['GET', 'POST'])
def goodList(request):
    if request.method == "GET":
        seria = GoodSerizlizer(instance=Good.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        seria = GoodSerizlizer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:

            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def goodDetail(request, cid):
    model = get_object_or_404(Good, pk=cid)
    if request.method == "GET":
        seria = GoodSerizlizer(instance=model)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT' or request.method == 'PATCH':
        seria = GoodSerizlizer(instance=model, data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse('没有此项')


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


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer
