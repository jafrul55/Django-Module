from django.urls import path
from .views import (
    UserRegistrationView,
    CreateUser,
    # BookListView,
    # BookSearchView,
    # BookReserveView,
    # BookBorrowView,
    # BookReturnView,
    # WishlistAddView,
    # WishlistRemoveView,
)

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register1'),
    path('res/',CreateUser.as_view()),
    # path('book_list/',BookListView.as_view(),name='book_list1'),
    # path('book_search/',BookSearchView.as_view(),name='book_search1'),
    # path('book_reserve/<int:pk>/',BookReserveView.as_view(),name='book_reserve1'),
    # path('book_borrow/<int:pk>/',BookBorrowView.as_view(),name='book_borrow1'),
    # path('book_return/<int:pk>/',BookReturnView.as_view(),name='book_return1'),
    # path('wishlist_add/<int:pk>/',WishlistAddView.as_view(),name='wishlist_add1'),
    # path('wishlist_remove/<int:pk>/',WishlistRemoveView.as_view(),name='wishlist_remove1')
]


