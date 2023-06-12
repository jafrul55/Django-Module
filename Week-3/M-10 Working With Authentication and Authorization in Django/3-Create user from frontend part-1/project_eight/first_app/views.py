from django.shortcuts import render
from first_app.forms import RegisterForm

# Create your views here.

def home(request):
    if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                # print(form.cleaned_data)
    else:
        form = RegisterForm()
    return render(request,'home.html',{'Form':form})
