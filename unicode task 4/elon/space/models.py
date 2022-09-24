from django.db import models

# Create your models here.
class SpaceX(models.Model):
    Name=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Field=models.CharField(max_length=100)