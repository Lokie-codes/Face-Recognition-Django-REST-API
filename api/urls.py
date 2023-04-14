# Path: api/views.py

from django.urls import path
from .views import (
    apiOverview,
    CourseList,
    BranchList,
    SemesterList,
    SectionList,
    StudentList,
    SubjectList,
    AttendanceList,
    CourseDetail,
    BranchDetail,
    SemesterDetail,
    SectionDetail,
    StudentDetail,
    SubjectDetail,
    AttendanceDetail,
)
from .send_mail import send_mail_to_parent

urlpatterns = [
    path("", apiOverview, name="api-overview"),
    path("course/", CourseList.as_view(), name="course-list"),
    path("course/<str:pk>/", CourseDetail.as_view(), name="course-detail"),
    path("branch/", BranchList.as_view(), name="branch-list"),
    path("branch/<str:pk>/", BranchDetail.as_view(), name="branch-detail"),
    path("semester/", SemesterList.as_view(), name="semester-list"),
    path("semester/<str:pk>/", SemesterDetail.as_view(), name="semester-detail"),
    path("section/", SectionList.as_view(), name="section-list"),
    path("section/<str:pk>/", SectionDetail.as_view(), name="section-detail"),
    path("student/", StudentList.as_view(), name="student-list"),
    path("student/<str:pk>/", StudentDetail.as_view(), name="student-detail"),
    path("subject/", SubjectList.as_view(), name="subject-list"),
    path("subject/<str:pk>/", SubjectDetail.as_view(), name="subject-detail"),
    path("attendance/", AttendanceList.as_view(), name="attendance-list"),
    path("attendance/<str:pk>/", AttendanceDetail.as_view(), name="attendance-detail"),
    path("send_mail/", send_mail_to_parent, name="send-mail"),
 ]
