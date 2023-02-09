from django.contrib import admin
from django.urls import path
from jobweb import views

urlpatterns = [
    path("", views.home, name='home'),
    path("home", views.home, name='home'),
    path("home2", views.home2, name='home2'),
    path("details", views.details, name='details'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("loguser", views.loguser, name='loguser'),
    path("login1", views.login1, name='login1'),
    path("register", views.register, name='register'),
    path("register1", views.register1, name='register1')
]