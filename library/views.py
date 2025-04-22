from django.shortcuts import render
from django.urls import reverse_lazy

from library.models import Book, Author
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BookListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(publication_date__year__gt=2000)


class BookCreateView(CreateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'publication_date', 'author']
    success_url = reverse_lazy('library:books_list')


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books_count'] = Book.objects.filter(author=self.object.author).count()
        return context


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

