# ProjectName:Ldemo001
# FileName:forms
# author:asus
# datetime:2020/2/19 9:50
# software: PyCharm
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, min_length=3, label="请输入用户名", help_text="用户名最小3个字符，最大150")
    password = forms.CharField(max_length=150, min_length=3, label='请输入密码', help_text='请规范输入密码3~150位')


class RegistForm(forms.ModelForm):
    password2 = forms.CharField(max_length=150, min_length=3, label="重复密码")

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {"username": "用户名",
                  "password": "密码",
                  }
