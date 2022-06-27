from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog) #주소/admin 사이트에서 Blog객체 확인가능하대
admin.site.register(Comment)