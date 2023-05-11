# Path: face/views.py

from django.urls import path
from .views import (
    faceOverview,
    FaceCount,
    FaceDetect,
    FaceRecognise,
)

urlpatterns = [
    path("", faceOverview, name="face-overview"),
    path("count/", FaceCount.as_view(), name="face-count"),
    path("faces/", FaceDetect.as_view(), name="face-detect"),
    path("recognise/", FaceRecognise.as_view(), name="face-recognise"),
]
