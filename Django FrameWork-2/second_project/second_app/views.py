from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def courses(request):
    return HttpResponse('''
                        <h1>There are all courses available</h1>
                        <a href = '/second_app/feedback/'>Feedback</a>
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/first_app/about/'>About</a>
                        <a href = '/''/'>Home</a>
                        
                        
                        
                        
                        ''')


def feedback(request):
    return HttpResponse('''
                        <h1>This is a feedback box</h1>
                        <a href = '/second_app/courses/'>Courses</a>
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/first_app/about/'>About</a>
                        <a href = '/''/'>Home</a>
                        ''')
