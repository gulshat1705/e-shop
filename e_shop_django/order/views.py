from itertools import product
import stripe

from django.conf import settings

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer, OrderItemSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            charge = stripe.Charge.create(
                amount = int(paid_amount * 100),
                currency = 'USD',
                description = 'Charge from e-Kids Shop',
                source = serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception:
            return Response(serializer.errors, status=status.HTTP_201_CREATED)  

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)

        return Response(serializer.data)



class Bestseller(APIView):

    def get(self, request, format=None):
        serializer = OrderItemSerializer(data=request.data)

        if serializer.is_valid():
            quantity = sum(item.get('quantity') + item.get('product').sold_count for item in serializer.validated_data['items'])

            serializer.save(quantity=quantity)

            return Response(serializer.data)