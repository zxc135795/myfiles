from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
# Django后台管理

from .models import Book, Hero, User,Account,Contact


class HeroInline(admin.StackedInline):
    model = Hero
    extra = 1


class HeroAdmin(ModelAdmin):
    list_display = ('name', 'gender', 'content', 'book')
    search_fields = ('name', 'gender', 'content')
    list_filter = ('name', 'gender', 'content')


class BookAdmin(ModelAdmin):
    list_display = ('title', 'price', 'pub_date')
    search_fields = ('title', 'price')
    list_filter = ('title', 'price')
    inlines = [HeroInline]


admin.site.register(Hero, HeroAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Contact)

