# ProjectName:Ldemo002
# FileName:feed
# author:asus
# datetime:2020/2/21 15:38
# software: PyCharm
from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import *


class ArticleFeed(Feed):
    title = '中冠'
    descripiton = '最新更新'
    link = '/'

    def items(self):
        return Article.objects.all().order_by('-create_time')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.author

    def item_link(self, item):
        url = reverse('blogapp:detail', args=(item.id,))
        return url
