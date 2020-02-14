# ProjectName:Ldemo001
# FileName:urls
# author:asus
# datetime:2020/2/13 14:36
# software: PyCharm
"""
引入绑定路由
"""
from django.conf.urls import url

from . import views

app_name = "booktest"
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletebook/(\d+)/$', views.deletebook, name='deletebook'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),

]
