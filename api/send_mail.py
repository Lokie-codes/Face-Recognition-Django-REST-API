from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Student, Attendance
from rest_framework.decorators import api_view

# Emailing the parents email with the attendance of the student
@api_view(["GET", "POST"])
def send_mail_to_parent(request):
    # students = Student.objects.filter("parentEmail")
    attendances = Attendance.objects.all()
    # for student in students:
    #     print(student)
    for attendance in attendances:
        # print(attendance)
        if attendance.status == True:
            present = "Present"
        else:
            present = "Absent"
        send_mail(
            "Attendance",
            f"Your child {attendance.student.fullName} is {present} today for the subject {attendance.subject.subjectName}",
            settings.EMAIL_HOST_USER,
            [attendance.student.parentEmail],
            fail_silently=False,
        )
    return HttpResponse(attendances)
