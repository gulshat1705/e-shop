from unittest import result
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
            'get_sale_price'            
        )


from collections import OrderedDict
class SaleProductSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
       result = super(SaleProductSerializer, self).to_representation(instance)
       return OrderedDict([key, result[key]] for key in result if result[key] is not None)
    class Meta:
        model = Product
        fields = (
            'id', 
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
            'get_sale_price'            
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