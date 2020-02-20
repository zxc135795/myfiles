# ProjectName:Ldemo002
# FileName:urls
# author:asus
# datetime:2020/2/20 9:28

from django.conf.urls import url
from . import views

app_name = 'blogapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^favicon.ico/$',views.favicon),
    url(r'^contact/$', views.contact, name='contact'),

]
