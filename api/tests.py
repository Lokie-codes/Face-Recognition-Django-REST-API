# write the test cases

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, Branch, Semester, Section, Student, Subject, Attendance


class CourseTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(courseName="B.Tech", courseCode="BTECH")

    def test_course_creation(self):
        self.assertTrue(isinstance(self.course, Course))
        self.assertEqual(self.course.__str__(), self.course.courseCode + " " + self.course.courseName)
        self.assertEqual(self.course.get_absolute_url(), reverse("Course_detail", kwargs={"pk": self.course.pk}))

    def test_course_list_view(self):
        response = self.client.get(reverse("Course_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.courseName)
        self.assertTemplateUsed(response, "api/course_list.html")

    def test_course_detail_view(self):
        response = self.client.get(reverse("Course_detail", kwargs={"pk": self.course.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.courseName)
        self.assertTemplateUsed(response, "api/course_detail.html")


class BranchTest(TestCase):
    def setUp(self):
        self.branch = Branch.objects.create(branchName="Computer Science and Engineering", branchCode="CSE")

    def test_branch_creation(self):
        self.assertTrue(isinstance(self.branch, Branch))
        self.assertEqual(self.branch.__str__(), self.branch.branchCode + " " + self.branch.branchName)
        self.assertEqual(self.branch.get_absolute_url(), reverse("Branch_detail", kwargs={"pk": self.branch.pk}))

    def test_branch_list_view(self):
        response = self.client.get(reverse("Branch_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.branch.branchName)
        self.assertTemplateUsed(response, "api/branch_list.html")

    def test_branch_detail_view(self):
        response = self.client.get(reverse("Branch_detail", kwargs={"pk": self.branch.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.branch.branchName)
        self.assertTemplateUsed(response, "api/branch_detail.html")


class SemesterTest(TestCase):
    def setUp(self):
        self.semester = Semester.objects.create(semesterName=1)

    def test_semester_creation(self):
        self.assertTrue(isinstance(self.semester, Semester))
        self.assertEqual(self.semester.__str__(), "semester " + str(self.semester.semesterName))
        self.assertEqual(self.semester.get_absolute_url(), reverse("Semester_detail", kwargs={"pk": self.semester.pk}))

    def test_semester_list_view(self):
        response = self.client.get(reverse("Semester_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.semester.semesterName)
        self.assertTemplateUsed(response, "api/semester_list.html")

    def test_semester_detail_view(self):
        response = self.client.get(reverse("Semester_detail", kwargs={"pk": self.semester.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.semester.semesterName)
        self.assertTemplateUsed(response, "api/semester_detail.html")


class SectionTest(TestCase):
    def setUp(self):
        self.section = Section.objects.create(sectionName="A")

    def test_section_creation(self):
        self.assertTrue(isinstance(self.section, Section))
        self.assertEqual(self.section.__str__(), self.section.sectionName)
        self.assertEqual(self.section.get_absolute_url(), reverse("Section_detail", kwargs={"pk": self.section.pk}))

    def test_section_list_view(self):
        response = self.client.get(reverse("Section_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.section.sectionName)
        self.assertTemplateUsed(response, "api/section_list.html")

    def test_section_detail_view(self):
        response = self.client.get(reverse("Section_detail", kwargs={"pk": self.section.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.section.sectionName)
        self.assertTemplateUsed(response, "api/section_detail.html")


class StudentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(courseName="B.Tech", courseCode="BTECH")
        self.branch = Branch.objects.create(branchName="Computer Science and Engineering", branchCode="CSE")
        self.semester = Semester.objects.create(semesterName=1)
        self.section = Section.objects.create(sectionName="A")
        self.student = Student.objects.create(user=self.user, course=self.course, branch=self.branch,
                                              semester=self.semester, section=self.section, rollNo=1)

    def test_student_creation(self):
        self.assertTrue(isinstance(self.student, Student))
        self.assertEqual(self.student.__str__(), self.student.usn)
        self.assertEqual(self.student.get_absolute_url(), reverse("Student_detail", kwargs={"pk": self.student.pk}))

    def test_student_list_view(self):
        response = self.client.get(reverse("Student_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student.usn)
        self.assertTemplateUsed(response, "api/student_list.html")

    def test_student_detail_view(self):
        response = self.client.get(reverse("Student_detail", kwargs={"pk": self.student.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student.usn)
        self.assertTemplateUsed(response, "api/student_detail.html")


