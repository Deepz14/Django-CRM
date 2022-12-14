from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
      model = Product
      fields = ['id',  'owner', 'name', 'price', 'description', 'category', 'brand', 'stock']
