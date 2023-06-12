from django.urls import path
from first_app.views import home, signup, Userlogin, profile

urlpatterns = [

    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', Userlogin, name='login'),
    path('profile/', profile, name='profile')

]
