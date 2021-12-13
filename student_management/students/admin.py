from django.contrib import admin

# Register your models here.
from .models import Students, Grade

admin.site.register(Students)
admin.site.register(Grade)