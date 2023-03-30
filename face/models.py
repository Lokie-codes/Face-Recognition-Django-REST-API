from django.db import models

# Create your models here.
class FaceImage(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/')