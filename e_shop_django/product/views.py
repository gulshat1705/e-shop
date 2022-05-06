from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer, SaleProductSerializer

from rest_framework.generics import GenericAPIView


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]       # late 4 products
        serializer = ProductSerializer(products, many=True)     # many objects

        return Response(serializer.data)                # return result


from rest_framework import generics
from django.db.models import F, Func
class SaleList(APIView):
    def get(self, request, format=None):
       # queryset = Product.objects.all()
        products = Product.objects.exclude(sale__isnull=True).exclude(sale__exact=0)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


       # sale = self.request.query_params.get('get_sale_price') or None
     #   if sale is not None:
       #     queryset = queryset.filter(product__get_sale_price=sale)
        #    return queryset
      #  return queryset.filter(product__get_sale_price=sale) 

  

#    Stats.objects.exclude(stats__isnull=True).exclude(stats__exact='')


class AllProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try: 
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404    


    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)

        return Response(serializer.data)     


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try: 
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404


    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)  

        return Response(serializer.data)      


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    else:
        return Response({'products': []})



  