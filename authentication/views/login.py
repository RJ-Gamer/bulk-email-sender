"""
Login Viewset
"""
import logging

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers.login import LoginSerializer
from common import constants

log = logging.getLogger(__name__)


class LoginViewSet(viewsets.ViewSet):
    """
    Login Viewset
    """

    serializer_class = LoginSerializer

    def create(self, request):
        """
        Post request for login

        parameters:
        --------------------------
        username(str): username
        password(str): password
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        refresh = RefreshToken.for_user(user)
        log.info(constants.LOG_LOGIN_SUCCESS)
        return Response(
            {
                "message": constants.MSG_SUCCESS.format(constants.LOGGED_IN),
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": user.username,
            },
            status=status.HTTP_200_OK,
        )
