from django.urls import path, include
# from library.views import books_list, books_detail
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


app_name = 'library'


urlpatterns = [
    path('books/', BookListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    # path('books_list/', books_list, name='books_list'),
    # path('book_detail/<int:book_id>/', books_detail, name='book_detail'),
]
