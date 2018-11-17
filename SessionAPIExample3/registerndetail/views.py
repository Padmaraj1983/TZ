from django.shortcuts import render
from registerndetail.forms import EmployeeForm
from . import forms
# Create your views here.
def emp_admin_view(request):
    form=EmployeeForm()
    emp_list
    if request.method=='POST':
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'registerndetail/EmployeeRegister.html',{'form':form})

def thanks_view(request):
    return render(request,'registerndetail/EmployeeRegister.html')




