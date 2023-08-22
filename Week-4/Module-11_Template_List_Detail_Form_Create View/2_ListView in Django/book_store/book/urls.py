from django.urls import path
# from book.views import home,store_book,show_books,edit_book,delete_book
# shortcut:
from . import views
urlpatterns = [
    # path('',home),
    # path('',views.TemplateView.as_view(template_name = 'home.html')),
    path('<int:roll>/',views.MyTemplateView.as_view(),{'author': 'Korim'}),
    path('store_new_book/',views.store_book,name='storebook'),
    # path('show_books/',views.show_books,name='showbook'),
    path('show_books/',views.BookListView.as_view(),name='showbook'),
    path('edit_book/<int:id>',views.edit_book,name='editbook'),
    path('delete_book/<int:id>',views.delete_book,name='deletebook'),
  
]
