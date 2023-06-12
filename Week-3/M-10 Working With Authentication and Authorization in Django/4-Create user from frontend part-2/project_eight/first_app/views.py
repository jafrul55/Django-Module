from django.shortcuts import render
from first_app.forms import RegisterForm
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            # messages.warning(request, 'warning')
            # messages.info(request, 'information')
            form.save()
            print(form.cleaned_data)
    else:
        form = RegisterForm()
    return render(request, 'home.html', {'Form': form})
