from django.shortcuts import render
gto
# Create your views here.
def base_view(request):
    return render(request,"newsportal/base.html")