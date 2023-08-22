from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {"name": 'I am Jafrul', "mark": 89,
                                          'Courses': [
                                              {
                                                  'name': 'Jafrul',
                                                  'course': 'C++',
                                                  'gender': 'Male'
                                              },
                                              {
                                                  'name': 'Rahana',
                                                  'course': 'Python',
                                                  'gender': 'Female'
                                              },
                                              {
                                                  'name': 'Sulthana',
                                                  'course': 'C',
                                                  'gender': 'Female'
                                              }
                                          ]
                                          })
