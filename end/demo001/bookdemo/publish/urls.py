# ProjectName:Ldemo001
# FileName:urls
# author:asus
# datetime:2020/2/17 10:14
# software: PyCharm
from django.conf.urls import url
from . import views

app_name = 'publish'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^detail/(\d+)/$', views.detail, name='detail'),

    url(r'^detail/(?P<qid>\d+)/$', views.detail, name='detail'),
    url(r'^result/(\d+)/$', views.result, name='result')

    # url(r'^$',views.IndexView.as_view(),name='index'),
    # url(r'^detail/(?P<qid>\d+)/$',views.DetailView.as_view(),name='detail'),
    # url(r'^result/(\d+)/$',views.ResultView.as_view(),name='result')



]
