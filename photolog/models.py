from django.db import models

# Create your models here.
class Photolog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    description = models.TextField(max_length=1000)