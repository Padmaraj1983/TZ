from django.db import models
# Create your models here.
class Cart(models.Model):
    itemname=models.CharField(max_length=128)
    qty=models.IntegerField()
    price=models.FloatField()


