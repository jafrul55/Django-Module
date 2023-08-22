from typing import Any, Dict, List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
# Create your views here.

# Function based view


def home(request):
    return render(request, 'store_book.html')

# Class based view


class MyTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name': 'Rahim', 'age': 22}
        print(kwargs)
        context.update(kwargs)  # To update in dictionary
        print(context)
        return context

# def store_book(request):
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             # book.save(commit=False)
#             book.save()
#             print(book.cleaned_data)
#             return redirect('showbook')

#     else:
#         book = BookStoreForm()
#     return render(request,'store_book.html',{'Form':book})

# FormView


# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     success_url = reverse_lazy('show_books')

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         # return HttpResponse('Form Submitted')
#         return redirect('show_books')

# CreateView:
class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')

# Function view:
# def show_books(request):
#     book = BookStoreModel.objects.all()
#     print(book)
    # for item in book:
    #     print(item.first_published)
    # return render(request,'show_book.html',{'data':book})

# Class base View:


class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'booklist'
    # def get_queryset(self):
    # return BookStoreModel.objects.filter(author='Jafrul')
    # return BookStoreModel.objects.filter(id='3') #You can also find id
    # If you want to show context data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context = {'Rohim': BookStoreModel.objects.filter(author='Rohim')}
    #     context = {'Rohim': BookStoreModel.objects.all().order_by('author')} #To Show order_by(lexographical_Order)
    #     return context

    # To sort ordering
    # ordering = ['author']
    # To set categorywise
    # ordering = ['category']

    # To set id:
    # ordering = ['id']

    # To reverse id:
    # ordering = ['-id']
#   -----------------------------------------|
    # HomeWork:
    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'superuser.html'
        elif self.request.user.is_staff:
            template_name = ''
        else:
            template_name = self.template_name
        return [template_name]

    # --------------------------------------------------|


class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('showbook')
    return render(request, 'store_book.html', {'Form': form})


def delete_book(request, id):
    book = BookStoreModel.objects.get(pk=id).delete()
    return redirect('showbook')
