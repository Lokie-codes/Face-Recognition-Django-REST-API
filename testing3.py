# Path: face/tests/integration/test_views.py
import os
import tempfile
from io import BytesIO

from PIL import Image
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from retinaface import RetinaFace

from face.serializers import faceOverview, FaceCount, FaceDetect, FaceRecognise

class FaceIntegrationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.image = Image.new("RGB", (100, 100), color="red")
        self.image_file = BytesIO()
        self.image.save(self.image_file, "jpeg")
        self.image_file.seek(0)

    def test_face_overview(self):
        response = self.client.get(reverse("face_overview"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Face Count", response.data)

    def test_face_count(self):
        url = reverse("face_count")
        response = self.client.post(url, {"image": self.image_file})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)

    def test_face_detect(self):
        url = reverse("face_detect")
        response = self.client.post(url, {"image": self.image_file})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["faces"], [])

    def test_face_recognise(self):
        url = reverse("face_recognise")
        response = self.client.post(url, {"image": self.image_file})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["result"], [])


