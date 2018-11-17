from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsapp/index.html')

def moviesinfo(request):
    head_msg='Latest Movie Information'
    msg1 = 'Msg1'
    msg2 = 'Msg2'
    msg3 = 'Msg3'
    msg4 = 'Msg4'
    my_dict={
        'head_msg':head_msg,
        'm1':msg1,
        'm2':msg2,
        'm3':msg3
    }
    return render(request,'newsapp/news.html',context=my_dict)

def sportsinfo(request):
    return render(request,'newsapp/news.html')

def politicsinfo(request):
    return render(request,'newsapp/news.html')