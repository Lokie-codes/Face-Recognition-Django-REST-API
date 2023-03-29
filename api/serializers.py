# Path: api/urls.py

from rest_framework.serializers import ModelSerializer
from .models import (
    Course,
    Branch,
    Semester,
    Section,
    Student,
    Subject,
    Attendance,
)


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class SemesterSerializer(ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
