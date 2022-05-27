from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),        # auth
    path('api/v1/login/', TokenObtainPairView.as_view()),
    path('api/v1/', include('djoser.urls.authtoken')),      # auth
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('profiles.urls')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('order.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
