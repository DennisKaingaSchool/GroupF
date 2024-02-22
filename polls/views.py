from django.shortcuts import render,HttpResponse
from polls.models import Member
# Create your views here.

# def home(request):
#     return HttpResponse("Hellpo world")



def home(request):
    members = Member.objects.all()
    return  HttpResponse(members)


def about(request):
    return HttpResponse("this is about page")