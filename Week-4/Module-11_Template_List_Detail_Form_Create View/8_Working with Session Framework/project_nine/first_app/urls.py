from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home),
    # path('cookie/',views.set_cookie),
    path('get/',views.get_cookie),
    path('del/',views.delete_cookie),
    path('',views.set_session),
    path('getsession/',views.get_session),
    path('delsession/',views.delete_session),
    
]
