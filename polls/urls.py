from django.urls import path
from polls import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("members",views.members,name="members"),
    path("elections",views.elections,name="elections")
]