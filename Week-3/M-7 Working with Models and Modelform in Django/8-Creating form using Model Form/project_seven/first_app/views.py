from django.shortcuts import render
from first_app.forms import StudentForms
# Create your views here.


def home(request):
    std = StudentForms
    return render(request, 'home.html', {'form': std})
