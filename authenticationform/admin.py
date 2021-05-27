from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import My_User
from .models import My_post
# Register your models here
admin.site.register(My_User)
admin.site.register(My_post)