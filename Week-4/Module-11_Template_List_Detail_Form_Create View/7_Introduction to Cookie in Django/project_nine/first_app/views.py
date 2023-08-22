from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def home(request):
    response = render(request,'home.html')
    # response.set_cookie('name','Jafrul')
    # response.set_cookie('name','Karim')
    
    # #For keeping cookie in website base on second
    # response.set_cookie('name','Karim',max_age=10)
    response.set_cookie('name','karim',expires=datetime.utcnow()+timedelta(days=7))
    return response

# To see cookies in website
def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})

# To delete  cookie in website
def delete_cookie(request):
    response = render(request,'del.html')
    response.delete_cookie('name')
    return response