from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
# Create your views here.
def home_page_view(request):
    return render(request,'testapp/base.html')

@login_required
def java_exams_view(request):
    return render(request,'testapp/javaexams.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form=SignUpForm()
    return render(request,'testapp/signup.html',{'form':form})