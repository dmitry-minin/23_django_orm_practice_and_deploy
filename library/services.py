from library.models import Review


class BookService:

    @staticmethod
    def calculate_average_rating(book_id):
        """
        Calculate the average rating of a book based on its reviews.
        """
        reviews = Review.objects.filter(book_id=book_id)

        if not reviews:
            return None

        total_rating = sum(review.rating for review in reviews)
        return total_rating / reviews.count()

    @staticmethod
    def is_popular(book_id, threshold=4):
        """
        Determine if a book is popular based on the number of reviews.
        A book is considered popular if it has more than 10 reviews.
        """
        average_rating = BookService.calculate_average_rating(book_id)
        if average_rating is None:
            return None

        return average_rating >= threshold
