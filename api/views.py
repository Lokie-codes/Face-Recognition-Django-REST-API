from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Course,
    Branch,
    Semester,
    Section,
    Student,
    Subject,
    Attendance,
)
from .serializers import (
    CourseSerializer,
    BranchSerializer,
    SemesterSerializer,
    SectionSerializer,
    StudentSerializer,
    SubjectSerializer,
    AttendanceSerializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Course List": "/course/",
        "Course Detail View": "/course/<str:pk>/",
        "Branch List": "/branch/",
        "Branch Detail View": "/branch/<str:pk>/",
        "Semester List": "/semester/",
        "Semester Detail View": "/semester/<str:pk>/",
        "Section List": "/section/",
        "Section Detail View": "/section/<str:pk>/",
        "Student List": "/student/",
        "Student Detail View": "/student/<str:pk>/",
        "Subject List": "/subject/",
        "Subject Detail View": "/subject/<str:pk>/",
        "Attendance List": "/attendance/",
        "Attendance Detail View": "/attendance/<str:pk>/",
    }
    return Response(api_urls)


class CourseList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class SemesterList(generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SectionList(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
