from django.shortcuts import render
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from .serializers import ChangePasswordSerializer, ProfileUpdateSerializer

from users_app.models import User


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    


class ProfileUpdateView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileUpdateSerializer




