from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    sal=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

