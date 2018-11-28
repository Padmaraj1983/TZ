from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class BeginnersGuide(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=264,unique_for_date='publish')
    author = models.ForeignKey(User,related_name='Beginner_guide')
    body = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()
    text7 = models.TextField()
    text8 = models.TextField()
    publish= models.DateTimeField(default=timezone.now())
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

