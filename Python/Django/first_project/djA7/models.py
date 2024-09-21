from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    height = models.FloatField()
    weight = models.FloatField()
    dietary_preference = models.CharField(max_length=200)