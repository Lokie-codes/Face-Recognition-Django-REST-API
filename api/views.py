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
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Course List": "http://127.0.0.1:8000/api/course/",
        "Course Detail View": "http://127.0.0.1:8000/api/course/<str:pk>/",
        "Branch List": "http://127.0.0.1:8000/api/branch/",
        "Branch Detail View": "http://127.0.0.1:8000/api/branch/<str:pk>/",
        "Semester List": "http://127.0.0.1:8000/api/semester/",
        "Semester Detail View": "http://127.0.0.1:8000/api/semester/<str:pk>/",
        "Section List": "http://127.0.0.1:8000/api/section/",
        "Section Detail View": "http://127.0.0.1:8000/api/section/<str:pk>/",
        "Student List": "http://127.0.0.1:8000/api/student/",
        "Student Detail View": "http://127.0.0.1:8000/api/student/<str:pk>/",
        "Subject List": "http://127.0.0.1:8000/api/subject/",
        "Subject Detail View": "http://127.0.0.1:8000/api/subject/<str:pk>/",
        "Attendance List": "http://127.0.0.1:8000/api/attendance/",
        "Attendance Detail View": "http://127.0.0.1:8000/api/attendance/<str:pk>/",
        "Send Email": "http://127.0.0.1:8000/api/send_mail/",
    }
    return Response(api_urls)


class CourseList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BranchList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class SemesterList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SectionList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class StudentList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class AttendanceList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
