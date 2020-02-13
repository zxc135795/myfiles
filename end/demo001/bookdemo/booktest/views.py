from django.shortcuts import render

# Create your views here.
# 视图数据请求
from django.http import HttpResponse
from django.template import loader
from .models import Hero, Book


def index(request):
    # template = loader.get_template('index.html')
    books = Book.objects.all()
    # context = {"books": books}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'index.html', {'books': books})


def detail(request, bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book": book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {'book': book})


def list(request):
    return HttpResponse("列表详情")

# 使用模板
