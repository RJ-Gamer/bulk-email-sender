"""
User viewset
"""
from urllib import request
from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from authentication.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ["get", "put", "patch"]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        return self.request.user
