# ProjectName:Ldemo002
# FileName:myfun
# author:asus
# datetime:2020/2/21 9:17
# software: PyCharm

from django.template import Library
from ..models import *

register = Library()


@register.filter
def dateFormat(data):
    return '%D-%d-%d' % (data.year, data.month, data.day)


@register.filter
def authorFormat(author, info):
    return info + ':' + author.upper()


@register.simple_tag
def get_latestarticles(num=3):
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def get_latedates(num=3):
    dates = Article.objects.dates('create_time', 'month', 'DESC')[:num]
    return dates


@register.simple_tag
def get_latecategory():
    return Category.objects.all().order_by('-id')
@register.simple_tag
def get_taps():
    return Tag.objects.all().order_by('-id')