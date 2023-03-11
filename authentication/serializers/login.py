"""
Login serializer
"""

from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from common import constants


class LoginSerializer(serializers.Serializer):
    """
    Login serializer
    """

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """
        Validate serializer attributes
        """
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    attrs["user"] = user
                    return attrs
                raise serializers.ValidationError(_(constants.ERR_ACCOUNT_INACTIVE))
            raise serializers.ValidationError(_(constants.ERR_INVALID_LOGIN))
        raise serializers.ValidationError(_(constants.ERR_PROVIDE_CREDENTIALS))
