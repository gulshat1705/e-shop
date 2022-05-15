from django.urls import path
from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),

    path('bestseller/', views.Bestseller.as_view()),
    path('all-orders/', views.OrderItemList.as_view()),
  
]