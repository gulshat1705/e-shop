from django.urls import path, include

from profiles import views

from .views import ChangePasswordView, ProfileUpdateView


urlpatterns = [
 # path('profile/', views.ProfileViews.as_view()),
  path('change_password/', ChangePasswordView.as_view()),
  path('update_profile/', ProfileUpdateView.as_view()),

]
