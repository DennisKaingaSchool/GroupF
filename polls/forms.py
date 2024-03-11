from typing import Any
from polls.models import Member,CandidateElection,Election
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = "__all__"

class CandidateElectionForm(forms.ModelForm):
    class Meta:
        model = CandidateElection
        fields = "__all__"

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

   