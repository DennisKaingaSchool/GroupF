from django.urls import path
from polls import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("members",views.members,name="members"),
    path("member/create",views.member_create,name="member_create"),
    path("candidates",views.candidates,name="candidates"),
    path("candidate/create",views.candidate_create,name="candidate_create"),
    path('success/', views.uploadok, name = 'success'),
    path("elections",views.elections,name="elections"),
    path('login/', views.user_login, name='login'),
    # path('login-form/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]