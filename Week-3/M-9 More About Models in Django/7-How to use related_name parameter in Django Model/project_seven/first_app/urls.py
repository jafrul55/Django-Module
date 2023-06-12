from django.urls import path
# You can also use:
from first_app.views import home,showData

# from . import views

urlpatterns = [
    path('', home, name='homepage'),
    path('show/',showData,name='showData')
]
