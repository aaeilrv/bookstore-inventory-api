from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Book
from api.serializers import BookSerializer
from api.services.book import BookService

class BookViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for managing book inventory operations.
    Basic CRUD operations are provided by ModelViewSet.
    Additional custom actions with custom responses are defined.
    
    '''

    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer


    @action(detail=False, methods=["get"])
    def search(self, request):

        category = request.query_params.get('category', None)

        if not category or category.strip() == "":
            return Response({
                "error": "Category parameter cannot be empty."
            }, status=status.HTTP_400_BAD_REQUEST)

        books = BookService.search_by_category(category)

        return Response({
            "count": len(books),
            "category": category,
            "books": BookSerializer(books, many=True).data
        }, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"], url_path='low-stock')
    def low_stock(self, request):

        threshold = request.query_params.get('threshold', None)

        if not threshold or threshold.strip() == "":
            return Response({
                "error": "Threshold parameter cannot be empty."
            }, status=status.HTTP_400_BAD_REQUEST)

        books = BookService.search_by_lowstock(threshold)

        return Response({
            "count": len(books),
            "threshold": threshold,
            "books": BookSerializer(books, many=True).data
        }, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["post"], url_path='calculate-price')
    def calculate_price(self, request, pk=None):

        book = self.get_object()

        markup_percentage = 0.4
        exchange_rate, cost_local, updated_book = BookService.calculate_suggested_price( 
            markup_percentage,
            book
        )
    
        return Response({
            "book_id": str(updated_book.id),
            "cost_usd": updated_book.cost_usd,
            "exchange_rate": exchange_rate,
            "cost_local": cost_local,
            "margin_percentage": int(markup_percentage * 100),
            "selling_price_local": updated_book.selling_price_local,
            "currency": "VES",
            "calculation_timestamp": updated_book.updated_at,
        }, status=status.HTTP_200_OK)