# Generated by Django 4.1.7 on 2023-03-29 14:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("branchName", models.CharField(max_length=100)),
                ("branchCode", models.CharField(max_length=10)),
            ],
            options={
                "verbose_name": "Branch",
                "verbose_name_plural": "Branches",
                "ordering": ["branchName"],
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("courseName", models.CharField(max_length=100)),
                ("courseCode", models.CharField(max_length=10)),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
                "ordering": ["courseName"],
            },
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sectionName", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Section",
                "verbose_name_plural": "Sections",
                "ordering": ["sectionName"],
            },
        ),
        migrations.CreateModel(
            name="Semester",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("semesterName", models.IntegerField()),
            ],
            options={
                "verbose_name": "Semester",
                "verbose_name_plural": "Semesters",
                "ordering": ["semesterName"],
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subjectName", models.CharField(max_length=100)),
                ("subjectCode", models.CharField(max_length=10)),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.branch",
                        verbose_name="branch",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.course",
                        verbose_name="course",
                    ),
                ),
                (
                    "semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.semester",
                        verbose_name="semester",
                    ),
                ),
            ],
            options={
                "verbose_name": "Subject",
                "verbose_name_plural": "Subjects",
                "ordering": ["subjectName"],
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("teacherId", models.CharField(max_length=15)),
                ("fullName", models.CharField(max_length=250)),
                ("position", models.CharField(max_length=250)),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.branch",
                        verbose_name="Branch Name",
                    ),
                ),
                (
                    "subjects",
                    models.ManyToManyField(
                        blank=True, to="api.subject", verbose_name="subjects"
                    ),
                ),
            ],
            options={
                "verbose_name": "Teacher",
                "verbose_name_plural": "Teachers",
                "ordering": ["teacherId"],
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("usn", models.CharField(max_length=15)),
                ("fullName", models.CharField(max_length=250)),
                ("image", models.ImageField(null=True, upload_to="db_path/")),
                ("parentEmail", models.EmailField(max_length=254)),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.branch",
                        verbose_name="branch",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.course",
                        verbose_name="course",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.section",
                        verbose_name="section",
                    ),
                ),
                (
                    "semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.semester",
                        verbose_name="semester",
                    ),
                ),
                (
                    "subjects",
                    models.ManyToManyField(
                        blank=True, to="api.subject", verbose_name="subjects"
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
                "ordering": ["usn"],
            },
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("status", models.BooleanField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.student",
                        verbose_name="student",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.subject",
                        verbose_name="subject",
                    ),
                ),
            ],
            options={
                "verbose_name": "Attendance",
                "verbose_name_plural": "Attendance",
                "ordering": ["date"],
            },
        ),
    ]
