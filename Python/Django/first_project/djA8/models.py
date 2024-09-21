from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextFieldField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)