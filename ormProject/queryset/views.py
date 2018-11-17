from django.shortcuts import render
from queryset.models import Employee
# Create your views here.
def emp_view(request):
    employee=Employee.objects.all()
    return render(request,'queryset/home.html',{'employee':employee})
