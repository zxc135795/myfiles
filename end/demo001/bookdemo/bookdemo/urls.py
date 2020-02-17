"""bookdemo URL Configuration

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
from django.urls import path, include

'''
路由地址配置
每一个网址绑定一个视图函数，视图函数返回页面
MVT T视图 作用： 接受请求  处理数据 返回响应
总的路由配置文件 == 项目路由文件 使用include包含
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publish/', include('publish.urls', namespace='publish')),
    path('', include('booktest.urls', namespace='booktest')),


]
