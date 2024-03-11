from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from polls.models import Member,Campus,Course,CandidateElection,ElectoralPosition,Party,Election
from polls.forms import MemberForm,CandidateElectionForm,LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse, reverse_lazy
def home(request):
    members = Member.objects.all()
    context = {
        'members':members
    }
    return  render(request,'polls/home.html',context)

@login_required
def members(request):
    context={
        'members':Member.objects.all(),#SELECT * FROM members;,
        'campuses':Campus.objects.all(),
        'courses':Course.objects.all(),
        # "title":"Members"
    }
    return render(request,"polls/members/index.html",context=context)
@login_required
def candidates(request):
    context={
        'members': Member.objects.exclude(
    id__in=CandidateElection.objects.values('candidate_election_member')
),
        'positions': ElectoralPosition.objects.all(),
        'parties':Party.objects.all(),
        "active_election" : Election.objects.filter(election_is_active=True).first(),
        'candidates':CandidateElection.objects.all(),#SELECT * FROM members;,
        "title":"Candidates"
    }
    return render(request,"polls/candidates/index.html",context=context)

@login_required
def candidate_create(request):
    if request.method == 'POST':
        form  = CandidateElectionForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.data)
            form.save()
            return redirect(reverse("candidates"))
        else:
            print(form.errors)
            return redirect(reverse("candidates"))
    else:
        form  = CandidateElectionForm()
    return redirect(reverse("candidates"))

@login_required
def member_create(request):
    if request.method == 'POST':
        member_first_name = request.POST.get('member_first_name')
        member_lastname = request.POST.get('member_lastname')
        member_date_of_birth = request.POST.get('member_date_of_birth')
        member_contact = request.POST.get('member_contact')
        member_address = request.POST.get('member_address')
        member_campus = request.POST.get('member_campus')
        member_course = request.POST.get('member_course')
        member_rank = request.POST.get('member_rank')
        campus = Campus.objects.get(id=member_campus)
        course = Course.objects.get(id=member_course)

        hashed_password = make_password(member_first_name)
        user = User.objects.create(username=member_lastname, password=hashed_password)


        new_member = Member.objects.create(
            member_first_name=member_first_name,
            member_lastname=member_lastname,
            member_date_of_birth=member_date_of_birth,
            member_contact=member_contact,
            member_address=member_address,
            member_campus=campus,
            member_course=course,
            member_rank=member_rank,
            user=user
         
        )
        return redirect(reverse("members"))
        # else:
            # print(form.errors)
            # return redirect(reverse("members"))
    else:
        form  = MemberForm()
    return redirect(reverse("members"))

def uploadok(request):
    return HttpResponse(' upload successful')
@login_required
def elections(request):
    context  ={
        'candidates':CandidateElection.objects.all(),
        'voters':Member.objects.all(),
        "title":"Elections"
    }
    return render(request,'polls/elections/index.html',context=context)


# login page
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)    
            print("I")
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'polls/login/index.html')

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


def login(request):
    return render(request,"polls/login/index.html")