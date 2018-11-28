from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from tradezone.models import BeginnersGuide
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
# Create your views here.
def home_page_view(request):
    return render(request,'tradezone/index.html')

def about_page_view(request):
    return render(request,'tradezone/about.html')

def index_page_view(request):
    return render(request,'tradezone/index.html')

# Create your views here.
def beginners_list_view(request):
    beginners_list=BeginnersGuide.objects.all()
    paginator = Paginator(beginners_list,3)
    page_number=request.GET.get('page')
    try:
        beginners_list = paginator.page(page_number)
    except PageNotAnInteger:
        beginners_list = paginator.page(1)
    except EmptyPage:
        beginners_list=paginator.page(paginator.num_pages)
    return render(request,'tradezone/beginners_list.html',{'beginners_list':beginners_list})


def beginners_detail_view(request,year,month,day,post):
    post=get_object_or_404(BeginnersGuide,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,'tradezone/beginners_detail.html',{'post':post})

def verifyBeforeInvest_view(request):
    return render(request,'tradezone/VbyouInvest.html')

def dti_view(request):
    return render(request,'tradezone/DTI.html')

def bestInvest_view(request):
    return render(request,'tradezone/BestInvest.html')