from django.db import models

class JobType(models.Model):
    jobName=models.CharField(max_length=30)
    jobType=models.CharField(max_length=30)
    jobLoc=models.CharField(max_length=30)

# Create your models here.
