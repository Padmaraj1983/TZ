from django.shortcuts import render
from . import forms
# Create your views here.

def register_view(request):
    form=forms.RegisterForm
    if request.method=='POST':
        form=forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'registerForm/register.html',{'form':form})