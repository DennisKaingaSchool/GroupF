from django.shortcuts import render,HttpResponse
from polls.models import Member
# Create your views here.

def home(request):
    members = Member.objects.all()
    context = {
        'members':members
    }
    return  render(request,'polls/home.html',context)


def members(request):
    return render(request,'polls/members/index.html')


def about(request):
    return HttpResponse("this is about page")

