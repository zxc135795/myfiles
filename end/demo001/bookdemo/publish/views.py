from django.shortcuts import render, redirect, reverse

# Create your views here.

# 视图数据请求
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choices

from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, qid):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=qid)
            return render(request, 'polls/detail.html', {"question": question})
        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")
    elif request.method == "POST":

        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes += 1
            choice.save()
            url = reverse("publish:result", args=(qid,))
            return redirect(to=url)
        except Exception as e:
            print(e)
            return HttpResponse("选项不合法")


def result(request, qid):
    try:
        question = Question.objects.get(id=qid)
        return render(request, 'polls/result.html', {"question": question})
    except:
        return HttpResponse("问题不合法")


# 基于CBV的形式实现首页
class IndexView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "polls/index.html"
    # queryset 指明返回的结果列表
    queryset = Question.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "questions"

    # 方法一、继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Question.objects.all()}


class DetailView(View):
    def get(self, request, qid):
        try:
            question = Question.objects.get(id=qid)
            print(question, "--")
            # 使用render发起一起请求
            return render(request, 'polls/detail.html', {"question": question})

        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")

    def post(self, request, qid):
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes += 1
            choice.save()
            url = reverse("publish:result", args=(qid,))
            return redirect(to=url)
        except:
            return HttpResponse("选项不合法")


class ResultView(View):
    def get(self, request, qid):
        try:
            question = Question.objects.get(id=qid)
            return render(request, 'polls/result.html', {"question": question})
        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")
