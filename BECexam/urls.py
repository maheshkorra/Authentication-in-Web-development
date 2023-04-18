from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('index',views.index,name="index"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('signup',views.signup,name="signup"),
    path('signuppagecss',views.signuppagecss,name="signuppagecss")

  ]