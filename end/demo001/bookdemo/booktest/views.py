from django.shortcuts import render, redirect, reverse

# Create your views here.
# 视图数据请求
from django.http import HttpResponse, HttpResponseRedirect
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


def deletebook(request, bookid):
    # 删除处理
    book = Book.objects.get(id=bookid)
    book.delete()
    url = reverse('booktest:index')
    return redirect(to=url)


def deletehero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()
    url = reverse('booktest:detail', args=(bookid,))  # args 里为元组 （'a',)
    return redirect(to=url)


def addhero(request, bookid):
    if request.method == 'GET':
        return render(request, 'addhero.html')
    elif request.method == 'POST':
        hero = Hero()
        hero.name = request.POST.get('heroname')
        hero.content = request.POST.get('content')
        hero.gender = request.POST.get('sex')
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse('booktest:detail', args=(bookid,))
        return redirect(to=url)


def edithero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    if request.method == 'GET':
        return render(request, 'edithero.html', {'hero': hero})
    elif request.method == 'POST':
        hero.name = request.POST.get('heroname')
        hero.gender = request.POST.get('sex')
        hero.content = request.POST.get('content')
        hero.save()
        url = reverse('booktest:detail', args=(hero.book.id,))
        return redirect(to=url)


def editbook(request, bookid):
    book = Book.objects.get(id=bookid)
    book.pub_date = str(book.pub_date)
    if request.method == 'GET':
        return render(request, 'editbook.html', {'book': book})
    elif request.method == 'POST':
        book.title = request.POST.get('booktitle')
        book.price = request.POST.get('price')
        book.pub_date = request.POST.get('update')
        book.save()
        # url = reverse('booktest:index', args=(bookid,))
        return redirect(to='/')


def list(request):
    return HttpResponse("列表详情")

# 使用模板
