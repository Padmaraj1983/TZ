from django.shortcuts import render
from filterapp.models import FilterDemo
# Create your views here.
def upper_view(request):
    data_list=FilterDemo.objects.all()
    return render(request,'filterapp/upper.html',{'data_list':data_list})

def lower_view(request):
    data_list=FilterDemo.objects.all()
    return render(request,'filterapp/lower.html',{'data_list':data_list})

def truncate_view(request):
    data_list=FilterDemo.objects.all()
    return render(request,'filterapp/truncate.html',{'data_list':data_list})