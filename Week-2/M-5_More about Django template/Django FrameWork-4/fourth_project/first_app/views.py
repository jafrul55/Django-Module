from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, './firstApp/home.html', {"name": "I am Rahim", "marks": 86,
                                                    "courses": [
                                                        {
                                                            "id": 1,
                                                            "course": "C",
                                                            "teacher": "Rahim"
                                                        },
                                                        {
                                                            "id": 2,
                                                            "course": "C++",
                                                            "teacher": "Karim"
                                                        },
                                                        {
                                                            "id": 3,
                                                            "course": "Python",
                                                            "teacher": "Hasan"
                                                        }
                                                    ]})


def about(request):
    return render(request, './firstApp/about.html', {"author": "glan Maxwell"})
