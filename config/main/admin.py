from django.contrib import admin

from .models import Class, Teacher, Student

# Register your models here.

admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)