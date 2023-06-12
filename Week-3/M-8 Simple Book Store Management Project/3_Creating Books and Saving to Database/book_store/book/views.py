from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.

def home(request):
    return render(request,'store_book.html')


def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
            book.save()
            return redirect('showbook')
    else:
        book = BookStoreForm()
    return render(request,'store_book.html',{'Form': book})

def show_book(request):
    book = BookStoreModel.objects.all()
    # To see time:
    # for item in book:
    #     print(item.first_published)
    print(book)
    return render(request,'show_book.html',{'data':book})