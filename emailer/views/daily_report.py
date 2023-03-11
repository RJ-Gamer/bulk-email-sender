"""
Model view set for daily reports
"""
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response

from emailer.serializers import DailyReportSerializer
from emailer.models import DailyReport


class DailyReportViewSet(viewsets.ModelViewSet):
    """
    Model view set for daily reports
    """

    serializer_class = DailyReportSerializer
    queryset = DailyReport.objects.all()
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
