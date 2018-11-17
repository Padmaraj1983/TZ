from django.db import models
class Registrations(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    PanNumber=models.CharField(max_length=30)
    uname=models.CharField(max_length=30)
    password=models.CharField(max_length=40)

# Create your models here.
