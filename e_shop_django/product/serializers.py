from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 
            'name',
            'get_absolute_url',
            'description',
            'price',
            'stock',
            'status',
            'sale',
            'get_image',
            'get_thumbnail',
            'get_sale_price', 
            'view_count',
            'sold_count'         
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)     # !!!!!!!!
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'products',             #related_name
        )