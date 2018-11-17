import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','BlrJobsSite.settings')
import django
django.setup()

from blrjobs.models import Jobtype
from faker import Faker
fakegen=Faker()

def populate(n):
    for i in range(n):
        jobName = models.CharField(max_length=30)
        jobType = models.CharField(max_length=30)
        jobLoc = models.CharField(max_length=30)
        fake_loc=fakegen.city()
        fake_jobName='Project Lead'
        fake_Type=fakegen.a
        jobs_record=Jobtype.objects.get_or_create(jobLoc=fake_loc,jobType=fake_tit,Desc=fake_Type,sal=fake_sal)
populate(100)
