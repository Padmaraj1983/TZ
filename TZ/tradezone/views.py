from django.shortcuts import render

# Create your views here.
# Create your views here.
def home_page_view(request):
    return render(request,'tradezone/index.html')

def about_page_view(request):
    return render(request,'tradezone/about.html')

def index_page_view(request):
    return render(request,'tradezone/index.html')

