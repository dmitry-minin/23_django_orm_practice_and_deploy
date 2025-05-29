from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ['last_name']


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    publication_date = models.DateField(verbose_name='Дата публикации')
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True, verbose_name='Рецензия')
    recommend = models.BooleanField(default=False, verbose_name='Рекомендовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['title']
        permissions = [
            ('can_review_book', 'Can review book'),
            ('can_recommend_book', 'Can recommend book'),
        ]


class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(blank=True, null=True, verbose_name='Rating')
    comment = models.TextField(blank=True, null=True, verbose_name='Comment')

    def __str__(self):
        return f'Review for {self.book.title}'

    class Meta:
        verbose_name = 'рецензия'
        verbose_name_plural = 'рецензии'
        ordering = ['rating']
