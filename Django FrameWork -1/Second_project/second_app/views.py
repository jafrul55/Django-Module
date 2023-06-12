from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home(request):
    return HttpResponse("<h2> I fear not the man who has practiced 10,000 kicks once, but I fear the man who has practiced one kick 10,000 times. Bruce Lee</h2>")


def Name(request):
    return HttpResponse("<h1>I am Jafrul Alam Tusar</h1>")


def Profession(request):
    return HttpResponse("<h1>I am a Software Engineer</h1>")


def Workplace(request):
    return HttpResponse("<h1>Google</h1>")


def Goal(request):
    return HttpResponse("<h1>CEO At Google")
