from django.http import HttpResponse


def Home(request):
    return HttpResponse('''
                        <h1>Welcome To My Home Page</h1>
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/first_app/about/'>About</a>
                        <a href = '/second_app/courses/'>Courses</a>
                        <a href = '/second_app/feedback/'>Feedback</a>
                        
                        ''')
