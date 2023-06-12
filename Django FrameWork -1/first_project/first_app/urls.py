from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('Allah/', views.Allah),
    path('Bangladesh/', views.Bangladesh),
    path('Google/', views.Google),
    path('University/', views.University)

]
