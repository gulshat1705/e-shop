from django.urls import path, include

from product import views


urlpatterns = [
    path('all-products/', views.AllProductList.as_view()),
    path('latest-products/', views.LatestProductList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    
    path('sale-products/', views.SaleList.as_view()),
    path('popular-products/', views.PopularProductList.as_view()),

 
]