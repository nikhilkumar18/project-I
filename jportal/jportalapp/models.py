from django.db import models
from django.db.models import Model

class jobs(models.Model):
    job      = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary =   models.IntegerField()
    workhours = models.CharField(max_length=100)
    contact =   models.IntegerField()

