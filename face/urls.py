# Path: face/views.py

from django.urls import path
from .views import (
    faceOverview,
    FaceCount,
    FaceDetect,
    FaceRecognise,
    FacePresent,
    FaceAbsent,
    FacePresentCount,
    FaceAbsentCount,
)

urlpatterns = [
    path("", faceOverview, name="face-overview"),
    path("count/", FaceCount.as_view(), name="face-count"),
    path("faces/", FaceDetect.as_view(), name="face-detect"),
    path("recognise/", FaceRecognise.as_view(), name="face-recognise"),
    path("present/", FacePresent.as_view(), name="face-present"),
    path("absent/", FaceAbsent.as_view(), name="face-absent"),
    path("present/count/", FacePresentCount.as_view(), name="face-present-count"),
    path("absent/count/", FaceAbsentCount.as_view(), name="face-absent-count"),
]
