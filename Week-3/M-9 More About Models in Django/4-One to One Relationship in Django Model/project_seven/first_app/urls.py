from django.urls import path
# You can also use:
from first_app.views import home

# from . import views

urlpatterns = [
    path('', home, name='homepage')
]
