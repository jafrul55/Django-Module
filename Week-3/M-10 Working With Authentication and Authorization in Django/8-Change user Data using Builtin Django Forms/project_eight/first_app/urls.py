from django.urls import path
from first_app.views import home, signup, Userlogin, profile, user_logout, pass_change, pass_changewithoutOldPass

urlpatterns = [

    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', Userlogin, name='login'),
    path('logout/', user_logout, name='logout'),
    path('passchange/', pass_change, name='passchange'),
    path('changepass/', pass_changewithoutOldPass, name='changepassword'),
    path('profile/', profile, name='profile')

]
