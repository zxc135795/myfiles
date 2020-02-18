from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from .models import *


class ChoicesInline(admin.StackedInline):
    model = Choices
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoicesInline]


class ChoicesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choices, ChoicesAdmin)
admin.site.register(User)
