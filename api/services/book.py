from api.models.book import Book
from api.services.external import ExternalService


class BookService:

    @classmethod
    def search_by_category(cls, category: str | None):
        '''
        Filters books by its category.
        Searches for exact matches, ignoring case sensitivity.

        Example:
        A search for "fiction" will return all books with category "Fiction",
        "fiction", "FICTION", etc, but will not return books with
        category "Science Fiction" or "Historical Fiction".

        An empty or null category will return an empty queryset.
        '''

        books = Book.objects.filter(
            category__iexact=category
        ).order_by("-title")

        return books
    
    @classmethod
    def search_by_lowstock(cls, threshold: int | None):
        '''
        Filters books with stock quantity below a specified threshold.

        An empty or null threshold will return an empty queryset.
        '''

        books = Book.objects.filter(
            stock_quantity__lte=threshold
        ).order_by("stock_quantity")

        return books
    
    @classmethod
    def calculate_suggested_price(cls, markup_percentage, book: Book) -> tuple[float, float, Book]:
        '''
        Calculates the local selling price for a book based
        on the current exchange rate amd a fixed markup percentage.

        returns the edited book object.
        '''

        exchange_rate = ExternalService.get_exchange_rate("VES")

        usd_cost = book.cost_usd
        cost_local = exchange_rate * usd_cost
        selling_price_local = cost_local + (cost_local * markup_percentage)

        book.selling_price_local = selling_price_local
        book.save()

        return exchange_rate, cost_local, book