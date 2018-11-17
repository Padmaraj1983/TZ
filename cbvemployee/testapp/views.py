from django.shortcuts import render
from testapp.models import Employee
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

class EmployeeListView(ListView):
    model=Employee

class EmployeeDetailView(DetailView):
    model=Employee

class EmployeeCreateView(CreateView):
    model=Employee
    fields=('eno','ename','sal')

class EmployeeUpdateView(UpdateView):
    model=Employee
    fields=('ename','sal')