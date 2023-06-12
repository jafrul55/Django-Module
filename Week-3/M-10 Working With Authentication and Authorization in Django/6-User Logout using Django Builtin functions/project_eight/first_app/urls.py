from django.urls import path
from first_app.views import home, signup, Userlogin, profile, user_logout

urlpatterns = [

    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', Userlogin, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile')

]
