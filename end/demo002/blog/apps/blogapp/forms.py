# ProjectName:Ldemo002
# FileName:forms
# author:asus
# datetime:2020/2/21 17:03
# software: PyCharm
from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'url', 'body', 'email']
        labels = {
            'name': '姓名',
            'url': '网址',
            'email': '邮箱'

        }
        widgets = {
            'body': forms.Textarea()
        }
