from django.db import models
# Create your models here.

class Register(models.Model):
    uname=models.EmailField()
    password=models.CharField(max_length=64)
    rpassword=models.CharField(max_length=64)

