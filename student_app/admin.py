from django.contrib import admin
from .models import Teacher, Student, Admission, Course
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Admission)
admin.site.register(Course)