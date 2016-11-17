from django.contrib import admin
from .models import Courses, Student

# Register your models here.


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'email')


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Student, StudentAdmin)
