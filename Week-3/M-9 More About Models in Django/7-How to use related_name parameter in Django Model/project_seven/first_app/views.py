from django.shortcuts import render
from first_app.forms import StudentForms
from first_app.models import Teacher,Student
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

# How to use related_name parameter in Django Model
def showData(request):
    # students list for one teacher:
    
    teacher = Teacher.objects.get(name = 'Tarek')
    students = teacher.student.all()
    for stud in students:
        # print(stud.name)
        print(stud.name,stud.roll,stud.class_name)
    
    # Teacher list for one student:
    
    student = Student.objects.get(name = 'Arnup')
    # teachers = student.teacher_set.all()
    # After using related_name teachers will be like this:
    teachers = student.teachers.all()
    for teacher in teachers:
        print(f"{teacher.name} {teacher.subject} {teacher.mobile}")
    return render(request,'show_data.html')
    
    
    # teachers list for one student