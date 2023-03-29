from django.contrib import admin
from .models import (
    Course,
    Branch,
    Semester,
    Section,
    Student,
    Subject,
    Attendance,
)

# Register your models here.
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Attendance)

