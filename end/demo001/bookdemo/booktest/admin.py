from django.contrib import admin

# Register your models here.
# Django后台管理

from .models import Book,Hero
admin.site.register(Book)
admin.site.register(Hero)