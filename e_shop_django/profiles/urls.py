from django.urls import path, include

from profiles import views

from .views import ChangePasswordView, ProfileUpdateView, ProfileViewSet


urlpatterns = [
  path('profile/<int:pk>/', views.ProfileViews.as_view()),
  path('change_password/<int:pk>/', ChangePasswordView.as_view()),
  path('update_profile/<int:pk>/', ProfileUpdateView.as_view()),
  path('profiles/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve'}))

]
