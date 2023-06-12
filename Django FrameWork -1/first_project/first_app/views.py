from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Hello,This is my first Django website</h1>")


def about(request):
    return HttpResponse("I am Jafrul Alam Tusar")


def University(request):
    return HttpResponse("<h1>National University</h1>")


def Google(request):
    return HttpResponse("<h1>Software Engineer</h1>")


def Bangladesh(request):
    return HttpResponse("<h2>I love My Bangledesh</h2>")


def Allah(request):
    return HttpResponse("<h1>I love my Allah</h1>")
