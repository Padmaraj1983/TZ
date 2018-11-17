import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormProject.settings')
import django
django.setup()

from queryset.models import Employee
from faker import Faker

fakegen=Faker()

def populate(n):
    for i in range(n):
        num=fakegen.random_int(min=30,max=n)
        name=fakegen.name()
        salary=fakegen.random_int()
        emp_record=Employee.objects.get_or_create(eno=num,ename=name,sal=salary)

populate(80)
