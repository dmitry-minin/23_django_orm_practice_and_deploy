from django.urls import path, include
# from library.views import books_list, books_detail
from .views import (BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, AuthorListView,
                    AuthorCreateView, AuthorUpdateView, RecommendBookView, ReviewBookView)


app_name = 'library'


urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),

    path('books/', BookListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('books/recommend/<int:pk>/', RecommendBookView.as_view(), name='book_recommend'),
    path('books/review/<int:pk>/', ReviewBookView.as_view(), name='book_review'),
]
