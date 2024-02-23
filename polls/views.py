from django.shortcuts import render,HttpResponse
from polls.models import Member,Campus,Course
# Create your views here.

def home(request):
    members = Member.objects.all()
    context = {
        'members':members
    }
    return  render(request,'polls/home.html',context)


def members(request):
    context={
        'members':Member.objects.all(),#SELECT * FROM members;,
        'campuses':Campus.objects.all(),
        'courses':Course.objects.all(),
        "title":"Members"
    }
    return render(request,"polls/members/index.html",context=context)
    

def elections(request):
    context  ={
        "title":"Elections"
    }
    return render(request,'polls/elections/index.html',context=context)
   
