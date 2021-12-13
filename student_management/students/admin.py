from django.contrib import admin

# Register your models here.
from .models import Grade, Students

admin.site.register(Students)
admin.site.register(Grade)
