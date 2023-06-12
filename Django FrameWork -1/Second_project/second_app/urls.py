from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('Name/', views.Name),
    path('Profession/', views.Profession),
    path('Workspace/', views.Workplace),
    path('Goal/', views.Goal)
]
