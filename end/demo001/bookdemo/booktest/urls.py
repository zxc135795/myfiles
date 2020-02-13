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

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^list/$', views.list),
    url(r'detail/(\d+)/',views.detail)

]
