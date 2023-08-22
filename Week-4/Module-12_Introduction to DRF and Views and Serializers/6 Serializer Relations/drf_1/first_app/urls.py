from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.StudentView.as_view()),
    # path('<int:pk>/',views.StudentDetailView.as_view()),


    path('',views.StudentListCreateView.as_view()),
    path('<int:pk>/',views.StudentRetrieveUpdateDestroyView.as_view()),
    path('course/',views.CourseListCreateView.as_view()),
    path('course/<int:pk>/',views.CourseRetrieveUpdateDestroyView.as_view(),name="course_details"),

    
]