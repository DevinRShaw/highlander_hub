from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    #intial idea of url to a view that renders a template 
    path("", views.index, name="index"),
    #importing a form and using as context for html
    path("register/", views.register, name = "register"),
    #already handled, now have to figure out how to access them
    path("accounts/", include("django.contrib.auth.urls")),
]