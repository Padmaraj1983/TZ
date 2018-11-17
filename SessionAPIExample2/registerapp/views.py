from django.shortcuts import render
from registerapp.forms import NameForm,AgeForm,GFForm

# Create your views here.
def name_view(request):
    form=NameForm()
    return render(request,"registerapp/name.html",{'form':form})

def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,"registerapp/age.html",{'form':form})
