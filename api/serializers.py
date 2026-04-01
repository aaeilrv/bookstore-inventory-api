from api.models.book import Book
from rest_framework import serializers
from django.core.exceptions import ValidationError
import re


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "isbn",
            "cost_usd",
            "selling_price_local",
            "stock_quantity",
            "category",
            "supplier_country",
            "created_at",
            "updated_at"
        ]
    
    def validate_isbn(self, value):
        """
        Validate ISBN format - must be 10 or 13 digits.
        """
        isbn_clean = re.sub(r'[-\s]', '', value)
        
        if not isbn_clean.isdigit():
            raise serializers.ValidationError("ERROR: ISBN must contain only digits (0-9).")

        if len(isbn_clean) not in [10, 13]:
            raise serializers.ValidationError("ERROR: ISBN must be exactly 10 or 13 digits long.")
        
        return value
    
    def validate_cost_usd(self, value):
        """
        Validate that cost_usd is greater than 0.
        """
        if value <= 0:
            raise serializers.ValidationError("ERROR: Cost in USD must be greater than 0.")
        return value
    
    def validate_stock_quantity(self, value):
        """
        Validate that stock_quantity is not negative.
        """
        if value < 0:
            raise serializers.ValidationError("ERROR:Stock quantity cannot be negative.")
        return value