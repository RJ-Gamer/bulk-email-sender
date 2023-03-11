"""
Email template view
"""
from operator import imod


import logging
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from emailer.serializers import EmailTemplateSerializer
from emailer.models import EmailTemplate

from common import constants

log = logging.getLogger(__name__)


class EmailTemplateViewSet(viewsets.ModelViewSet):
    """
    A viewset for email templates that provides CRUD operations (Create, Retrieve, Update and Delete).
    Only authenticated users can access this viewset.
    """

    serializer_class = EmailTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = EmailTemplate.objects.order_by("id")
    model = EmailTemplate

    def create(self, request, *args, **kwargs):
        """
        Handles HTTP POST requests to create an EmailTemplate instance.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email_template = serializer.save()
        log.info(constants.LOG_OBJ_CREATED.format(self.model.__name__))
        return Response(
            {
                "message": constants.MSG_CREATE_SUCCESS.format(self.model.__name__),
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        """
        Handles HTTP PUT or PATCH requests to update an existing EmailTemplate instance.
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        email_template = serializer.save()
        log.info(constants.LOG_OBJ_UPDATED.format(instance))
        return Response(
            {
                "message": constants.MSG_UPDATE_SUCCESS.format(self.model.__name__),
                "data": serializer.data,
            },
            status=status.HTTP_206_PARTIAL_CONTENT,
        )

    def destroy(self, request, *args, **kwargs):
        """
        Handles HTTP DELETE requests to delete an EmailTemplate instance.
        """
        instance = self.get_object()
        log.info(constants.LOG_OBJ_DELETED.format(self.model.__name__))
        self.perform_destroy(instance)
        return Response(
            {"message": constants.MSG_DELETE_SUCCESS.format(self.model.__name__)},
            status=status.HTTP_204_NO_CONTENT,
        )
