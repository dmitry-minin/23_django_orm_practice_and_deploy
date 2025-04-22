from django.shortcuts import render
from django.urls import reverse_lazy

from library.models import Book, Author
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BookListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'publication_date', 'author']
    success_url = reverse_lazy('library:books_list')


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'publication_date', 'author']
    success_url = reverse_lazy('library:books_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('library:books_list')

# def books_list(request):
#     books = Book.objects.all()
#     context = {
#         'books': books
#     }
#     return render(request, 'library/books_list.html', context=context)
#
#
# def books_detail(request, book_id):
#     book = Book.objects.get(id=book_id)
#     context = {
#         'book': book
#     }
#     return render(request, 'library/book_detail.html', context=context)
