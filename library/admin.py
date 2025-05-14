from django.contrib import admin
from library.models import Author, Book
from users.models import CustomUser


# admin.site.register(Author) вариант первый, ниже вариант 2
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author')
    list_filter = ('publication_date', 'author')
    search_fields = ('title', 'author__first_name', 'author__last_name')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('is_staff',)
    ordering = ('username',)