from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Article)
admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)


