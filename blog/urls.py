from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    home, 
    about, 
    # login, 
    register, 
    addpost, 
    profile, 
    profileupdate, 
    profileadd,
    like,
    updatepost,
    deletepost,
    postdetail,
    )

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('register', register, name='register'),

    # auth_views (login, logout)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # profile
    path('profile', profile, name='profile'),
    path('profileadd', profileadd, name='profileadd'),
    path('profileupdate', profileupdate, name='profileupdate'),

    # post
    path('addpost', addpost, name='addpost'),
    path('updatepost/<int:id>', updatepost, name='updatepost'),
    path('deletepost/<int:id>', deletepost, name='deletepost'),
    path('postdetail/<str:slug>', postdetail, name='postdetail'),


    # actions
    path('like/<int:id>', like, name='like'),
]