from django.urls import path
from polls import views

urlpatterns = [
    path("/home",views.home,name="home"),
    path("/about",views.about,name="about")
]