from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, Page


# 一个Page中有  object_list代表当前页的所有对象
# has_next 是不是有下一页
# has_previous 是否有上一页
# next_page_number 下一页的编号
# previous_page_number 上一页的编号
# self.number 当前页的编号
# self.paginator 当前页的分页器


# 一个Paginator中的object_list 代表所有未分页对象
# self.per_page 每一页有几个对象
# get_page(self, number): 从分页器中取第几页
# page_range(self): 返回分页列表


# Create your views here.
def index(request):
    ads = Ads.objects.all()
    typepage = request.GET.get('type')
    year = None
    month = None
    category_id = None
    tag_id = None
    if typepage == 'date':
        year = request.GET.get('year')
        month = request.GET.get('month')

        articles = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    elif typepage == 'category':
        category_id = request.GET.get('category_id')
        try:
            category = Category.objects.get(id=category_id)
            articles = category.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse('未找到内容')
    elif typepage == 'tag':
        tag_id = request.GET.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse('未知错误')

    else:
        articles = Article.objects.all().order_by('-create_time')

    paginator = Paginator(articles, 2)
    num = request.GET.get('pagenum', 1)
    page = paginator.get_page(num)
    return render(request,'index.html',locals())
    # return render(request, 'index.html', {'ads': ads, 'page': page, 'type': typepage, 'year': year, 'month': month})


def detail(request, id):
    return render(request, 'single.html', )


def contact(request):
    return render(request, 'contact.html')


def favicon(request):
    return redirect(to='/static/favicon.ico')
