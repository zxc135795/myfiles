from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view, action
from rest_framework import status, generics, mixins
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from . import permissions as mypermissions
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category
    serializer_class = CategorySerizlizer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category
    serializer_class = CategorySerizlizer


class CategoryListView11(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category
    serializer_class = CategorySerizlizer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailView11(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    queryset = Category
    serializer_class = CategorySerizlizer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


@api_view(['GET', 'POST'])
def categoryList(request):
    """
    基于函数视图自定义序列化
    :param request:
    :return:
    """
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


class CategoryListView1(APIView):
    def get(self, request):
        seria = CategorySerizlizer(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)

    def post(self, request, ):
        seria = CategorySerizlizer(data=request.data)

        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)


class CategoryDetailView1(APIView):
    def get(self, request, cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=cid))
        # seria.is_valid(raise_exception=True)
        # seria.save()
        return Response(seria.data, status=status.HTTP_200_OK)

    def put(self, request, cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)

    def patch(self, request, cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)

    def delete(self, request, cid):
        seria = get_object_or_404(Category, pk=cid)
        # seria.is_valid(raise_exception=True)
        seria.delete()
        return Response(seria.data, status=status.HTTP_204_NO_CONTENT)


class GoodListView(View):
    pass


class GoodDetailView(View):
    pass


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET POST PUT PATCh DELETE 等 HTTP 动词操作
    queryset 指明 操作模型

    """

    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

    # filter_backends = []
    filterset_fields = ['name']


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerizlizer


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer


class UserViewSets1(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
    声明用户资源类 用户操作： 获取个人信息  更新个人信息   删除账户
    扩展出action路由   用户操作：  创建账户
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 使用action扩展资源的http方法
    @action(methods=["POST"], detail=False)
    def regist(self, request):
        seria = UserRegistSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)


class UserViewSets(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    """
    声明用户资源类 用户操作： 获取个人信息  更新个人信息   删除账户
    扩展出action路由   用户操作：  创建账户
    """
    queryset = User.objects.all()

    # serializer_class = UserSerializer

    def get_serializer_class(self):
        print("action代表http方法", self.action)
        if self.action == "create":
            return UserRegistSerializer
        return UserSerializer


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    # permission_classes = [permissions.OrdersPermission]

    def get_permissions(self):
        """
        超级管理员只可以展示所有订单
        普通用户 可以创建修改订单 不可以操作其他用户的订单
        :return:
        """
        print("http方法为", self.action)
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            return [mypermissions.OrdersPermission()]
        else:
            return [permissions.IsAdminUser()]
