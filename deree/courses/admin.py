from django.contrib import admin

from .models import Student
from .models import Course
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass