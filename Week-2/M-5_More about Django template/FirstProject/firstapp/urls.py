from django.shortcuts import render
from django.urls import path
from .views import home

urlpatterns = [
    path('first/', home)
]
