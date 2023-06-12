from django.shortcuts import render
from first_app.forms import StudentForms
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            # For not save use: commit=False
            # For save function
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForms()
    return render(request, 'home.html', {'Form': form})
