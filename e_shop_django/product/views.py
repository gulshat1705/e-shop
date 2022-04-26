from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from product import serializers


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]       # late 4 products
        serializer = ProductSerializer(products, many=True)     # many objects
        return Response(serializer.data)                # return result


class ProductDetail(APIView):
    pass




