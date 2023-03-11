"""
Model view set for daily reports
"""
from rest_framework import status, permissions, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from emailer.serializers import DailyReportSerializer
from emailer.models import DailyReport
from emailer.filters import DailyReportFilter


class DailyReportViewSet(viewsets.ModelViewSet):
    """
    Model view set for daily reports
    """

    serializer_class = DailyReportSerializer
    queryset = DailyReport.objects.order_by("id")
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["record_date"]
    filter_class = DailyReportFilter
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
