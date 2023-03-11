"""
User serializer
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    User model serializer
    """

    class Meta:
        """User model meta information"""

        model = User
        exclude = ("password", "groups", "user_permissions")
