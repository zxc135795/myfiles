"""drfend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from shop.views import *
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT
# 模板result自带API路由模块 routers
from rest_framework import routers

from rest_framework.documentation import include_docs_urls

"""
前后端分离 常用库Djangorestframework

设置result 默认路由 router = routers.DefaultRouter()
注册路由 router.register('goods', GoodViewSets)
GoodViewSets 需在views模块中重写

"""
router = routers.DefaultRouter()
router.register('categorys', CategoryViewSets)
router.register('goods', GoodViewSets)
router.register('goodimgs', GoodImgsViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    url(r'^categorylist/$', categoryList, name='categorylist'),
    url(r'^categorydetail/(\d+)/$', categoryDetail, name='categorydetail'),
    url(r'^goodlist/$', goodList, name='goodlist'),
    url(r'^gooddetail/(\d+)/$', goodDetail, name='gooddetail'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    path('api/v1/docs/', include_docs_urls('RestFulAPI', description='RestFulAPI')),
    path('', include('rest_framework.urls')),

]
