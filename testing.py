from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course, Branch, Semester, Section, Student, Subject, Attendance
from .serializers import CourseSerializer, BranchSerializer, SemesterSerializer, SectionSerializer, StudentSerializer, SubjectSerializer, AttendanceSerializer


class CourseModelTestCase(TestCase):
    def setUp(self):
        self.course_name = "Computer Science"
        self.course = Course.objects.create(name=self.course_name)

    def test_course_model(self):
        self.assertEqual(self.course.courseName, self.course_name)


class CourseViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(name="Computer Science")
        self.course_url = "/course/"
        self.course_detail_url = f"{self.course_url}{self.course.pk}/"
        self.course_data = {"name": "Electrical Engineering"}

    def test_course_list_view(self):
        response = self.client.get(self.course_url)
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_detail_view(self):
        response = self.client.get(self.course_detail_url)
        course = Course.objects.get(pk=self.course.pk)
        serializer = CourseSerializer(course)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course_view(self):
        response = self.client.post(self.course_url, data=self.course_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_course_view(self):
        response = self.client.put(self.course_detail_url, data=self.course_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_course_view(self):
        response = self.client.delete(self.course_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class IntegrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_data = {"name": "Computer Science"}
        self.course_url = "/course/"
        self.course_detail_url = None

    def test_course_creation(self):
        response = self.client.post(self.course_url, data=self.course_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.course_detail_url = response.data.get("url")

    def test_course_update(self):
        if not self.course_detail_url:
            self.test_course_creation()

        new_course_data = {"name": "Electrical Engineering"}
        response = self.client.put(self.course_detail_url, data=new_course_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), new_course_data.get("name"))

    def test_course_deletion(self):
        if not self.course_detail_url:
            self.test_course_creation()

        response = self.client.delete(self.course_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SystemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_data = {"name": "Computer Science"}
        self.course_url = "/course/"
        self.course_detail_url = None

    def test_api_overview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_send_mail(self):
        response = self.client.get("/send_mail/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_course_api(self):
        self.test_course_creation()
       
