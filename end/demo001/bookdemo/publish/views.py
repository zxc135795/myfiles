from django.shortcuts import render, redirect, reverse
# Create your views here.
# 视图数据请求
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choices, User
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login as lin, logout as lout


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, qid):
    if request.method == "GET":
        if request.user and request.user.username != '':
            try:
                question = Question.objects.get(id=qid)
                if question in request.user.questions.all():
                    url = reverse('publish:result', args=(qid,))
                    return redirect(to=url)
                # return render(request, 'polls/detail.html', {"question": question})
                else:
                    try:
                        return render(request, 'polls/detail.html', {"question": question})
                    except Exception as e:
                        print(e)
                        return HttpResponse("问题不合法")
            except Exception as e:
                print(e)
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


def login(request):
    if request.method == 'GET':
        return render(request, 'polls/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            lin(request, user)
            url = reverse('publish:index')
            return redirect(to=url)
        else:
            url = reverse('publish:login')
            return redirect(to=url)


def logout(request):
    lout(request)
    url = reverse('publish:index')
    return redirect(to=url)


def regist(request):
    if request.method == 'GET':
        return render(request, 'polls/regist.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).count() > 0:
            return HttpResponse('用户名存在')
        else:
            if password == password2:
                User.objects.create_user(username=username, password=password)
                url = reverse('publish:login')
                return redirect(to=url)
            else:
                return HttpResponse('两次密码不一致')


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
