from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from library.forms import BookForm, AuthorForm
from library.models import Book, Author
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


class ReviewBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)

        if not request.user.has_perm('library.can_review_book'):
            return HttpResponseForbidden("You do not have permission to review this book.")

        book.review = request.POST.get('review')
        book.save()

        return redirect('library:book_detail', pk=pk)


class RecommendBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)

        if not request.user.has_perm('library.can_recommend_book'):
            return HttpResponseForbidden("You do not have permission to recommend this book.")

        book.recommend = True
        book.save()

        return redirect('library:book_detail', pk=pk)


class AuthorListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'library/authors_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        query_set = cache.get('authors_queryset')
        if not query_set:
            query_set = super().get_queryset()
            cache.set('authors_queryset', query_set, 60 * 15)
        return query_set


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'library/author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('library:authors_list')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'library/author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('library:authors_list')


@method_decorator(cache_page(60 * 15), name='dispatch')
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(publication_date__year__gt=2000)


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'library/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.add_book'


@method_decorator(cache_page(60 * 15), name='dispatch')
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books_count'] = Book.objects.filter(author=self.object.author).count()
        return context


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'library/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.change_book'


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.delete_book'
