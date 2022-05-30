from django.shortcuts import get_object_or_404, render
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from .serializers import ChangePasswordSerializer, ProfileUpdateSerializer

from users_app.models import User
from .models import Profile

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer

from rest_framework import permissions, generics, viewsets, response, mixins

from .permissions import (
    IsOwnerOrReadOnly, IsAdminUserOrReadOnly, IsSameUserAllowEditionOrReadOnly
)
class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    


class ProfileViews(generics.RetrieveAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        return Profile.objects.filter(id=self.requestuser.id)


    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)

        return obj

class ProfileUpdateView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileUpdateSerializer


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)  
