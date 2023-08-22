from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import Book,BookReservation,BookBorrowing,Wishlist
from datetime import datetime,timedelta,timezone
from django.urls import reverse_lazy

# class UserRegistrationView(View):
    # def post(self,request):
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         Wishlist.objects.create(user=user)
    #         return redirect('login')
    #     return render(request,'registration.html',{'form':form})
    
class UserRegistrationView(FormView):
    template_name = './library/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self,form):
        user = form.save()
        Wishlist.objects.create(user=user)
        return super().form_valid(form)
    
    
    
class CreateUser(View):
    def get(self,request):
        return render(request,'res.html')
    
# class BookListView(View):
#     def get(self,request):
#         books = Book.objects.all()
#         user = request.user
#         if user.is_authenticated:
#             wishlist = user.wishlist.book.all()
#             return render(request,'book_list.html',{'book':books,'wishlist':wishlist})
        
# class BookSearchView(View):
#     def get(self,request):
#         query = request.Get.get('q')
#         books = Book.objects.filter(title_icontains = query)
#         return render(request,'book_search.html',{'books':books})
    
# class BookReserveView(LoginRequiredMixin,View):
#     def post(self,request,pk):
#         book = Book.objects.get(pk=pk)
#         user = request.user
#         reservation = BookReservation.objects.create(user=user,book=book)
#         #You can add logic to send notifications to the user
#         return redirect('library:book_list')
    
# class BookBorrowView(LoginRequiredMixin,View):
#     def post(self,request,pk):
#         book = Book.objects.get(pk=pk)
#         user = request.user
#         borrowing = BookBorrowing.objects.create(user=user,book=book)
#         # Set the due date and implement borrowing logic
#         return redirect('library:book_list')
    
# class BookReturnView(LoginRequiredMixin,View):
#     def post(self,request,pk):
#         book = Book.objects.get(pk=pk)
#         user = request.user
#         borrowing = BookBorrowing.objects.get(user=user,book=book)
#         borrowing.return_date = timezone.now().date()
#         borrowing.save()
#         #Implement fine calculation logic
#         return redirect('library:book_list')
    
# class WishlistAddView(LoginRequiredMixin,View):
#     def post(self,request,pk):
#         book = Book.objects.get(pk=pk)
#         user = request.user
#         wishlist = user.wishlist
#         wishlist.book.add(book)
#         return redirect('library:book_list')
    
# class WishlistRemoveView(LoginRequiredMixin,View):
#     def post(self,request,pk):
#         book = Book.objects.get(pk=pk)
#         user = request.user
#         wishlist = user.wishlist
#         wishlist.book.remove(book)
#         return redirect('library:book_list')
        