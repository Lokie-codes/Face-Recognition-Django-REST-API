# Path: api/models.py
from django.db import models
from django.urls import reverse
import os


# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseCode = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.courseCode} {self.courseName}"

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["courseName"]


class Branch(models.Model):
    branchName = models.CharField(max_length=100)
    branchCode = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.branchCode} {self.branchName}"

    def get_absolute_url(self):
        return reverse("Branch_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
        ordering = ["branchName"]


class Semester(models.Model):
    semesterName = models.IntegerField()
    # semesterCode = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"semester {self.semesterName}"

    def get_absolute_url(self):
        return reverse("Semester_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Semester"
        verbose_name_plural = "Semesters"
        ordering = ["semesterName"]


class Section(models.Model):
    sectionName = models.CharField(max_length=100)
    # sectionCode = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.sectionName}"

    def get_absolute_url(self):
        return reverse("Section_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"
        ordering = ["sectionName"]


class Subject(models.Model):
    subjectName = models.CharField(max_length=100)
    subjectCode = models.CharField(max_length=10)
    course = models.ForeignKey(
        "Course", verbose_name="course", on_delete=models.CASCADE
    )
    branch = models.ForeignKey(
        "Branch", verbose_name="branch", on_delete=models.CASCADE
    )
    semester = models.ForeignKey(
        "Semester", verbose_name="semester", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.subjectCode} {self.subjectName}"

    def get_absolute_url(self):
        return reverse("Subject_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ["subjectName"]

def deleteRepresentationFile():
    os.remove(f"db_path/representations_vgg_face.pkl")

def renameImagePath(instance, filename):
    # name = instance.fullName.replace(" ", "_")
    usn = instance.usn
    # upload_to = "db_path/{}".format(usn)
    upload_to = "db_path/"
    extension = filename.split(".")[-1]
    filename = "{}.{}".format(usn, extension)
    # delete previous representations
    deleteRepresentationFile()
    return os.path.join(upload_to, filename)


class Student(models.Model):
    usn = models.CharField(max_length=15, unique=True)
    fullName = models.CharField(max_length=250)
    course = models.ForeignKey(
        "Course", verbose_name="course", on_delete=models.CASCADE
    )
    branch = models.ForeignKey(
        "Branch", verbose_name="branch", on_delete=models.CASCADE
    )
    semester = models.ForeignKey(
        "Semester", verbose_name="semester", on_delete=models.CASCADE
    )
    section = models.ForeignKey(
        "Section", verbose_name="section", on_delete=models.CASCADE
    )

    image = models.ImageField(null=True, upload_to=renameImagePath)
    parentEmail = models.EmailField()
    subjects = models.ManyToManyField("Subject", verbose_name=("subjects"), blank=True)

    def __str__(self) -> str:
        return f"{self.usn} {self.fullName} {self.course} {self.branch} section - {self.section}  {self.semester} "

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["usn"]


class Attendance(models.Model):
    student = models.ForeignKey(
        "Student", verbose_name="student", on_delete=models.CASCADE, to_field="usn"
    )
    subject = models.ForeignKey(
        "Subject", verbose_name="subject", on_delete=models.CASCADE
    )
    date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.date} {self.student} {self.subject} {self.status}"

    def get_absolute_url(self):
        return reverse("Attendance_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendance"
        ordering = ["date"]
