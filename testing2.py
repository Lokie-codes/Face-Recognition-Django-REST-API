# Path: face/tests/test_serializers.py
from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from PIL import Image

class FaceCountTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_count_faces(self):
        # Test when there are no faces in the image
        with patch('retinaface.RetinaFace.detect_faces', return_value=[]):
            response = self.client.post('/count/', {'image': Image.new('RGB', (100, 100)).tobytes()})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {'count': 0})

        # Test when there is one face in the image
        with patch('retinaface.RetinaFace.detect_faces', return_value=[{'box': [10, 10, 50, 50], 'confidence': 0.9}]):
            response = self.client.post('/count/', {'image': Image.new('RGB', (100, 100)).tobytes()})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {'count': 1})

class FaceDetectTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_detect_faces(self):
        # Test when there are no faces in the image
        with patch('retinaface.RetinaFace.detect_faces', return_value=[]):
            response = self.client.post('/faces/', {'image': Image.new('RGB', (100, 100)).tobytes()})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {'faces': []})

        # Test when there is one face in the image
        with patch('retinaface.RetinaFace.detect_faces', return_value=[{'box': [10, 10, 50, 50], 'confidence': 0.9}]):
            response = self.client.post('/faces/', {'image': Image.new('RGB', (100, 100)).tobytes()})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {'faces': [{'box': [10, 10, 50, 50], 'confidence': 0.9}]})


class FaceRecogniseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_recognise_faces(self):
        # Test when there are no faces in the image
        with patch('deepface.DeepFace.find', return_value=[{'identity': []}]):
            response = self.client.post('/recognise/', {'image': Image.new('RGB', (100, 100)).tobytes()})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {'result': []})

        # Test when there are faces in the image but not in the database
        with patch('deepface.DeepFace.find', return_value=[{'identity': ['db_path/foo.jpg', 'db_path/bar.jpg']}, ]):
            response = self.client.post('/recognise/', {'image': Image.new('RGB', (100, 100)).tobytes()})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {'result': []})

        # Test when there are faces in the image and they are in the database
        with patch('deepface.DeepFace.find', return_value=[{'identity': ['db_path/foo.jpg', 'db_path/bar.jpg']}, ]):
            with patch('os.path.abspath', return_value='/tmp/image.jpeg'):
                with patch('
