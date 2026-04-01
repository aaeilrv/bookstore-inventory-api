import uuid

from django.db import models


class Book(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    isbn=models.CharField(max_length=50, unique=True)
    cost_usd=models.FloatField()
    selling_price_local=models.FloatField(null=True, blank=True)
    stock_quantity=models.IntegerField()
    category=models.CharField(max_length=50)
    supplier_country=models.CharField(max_length=125)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)