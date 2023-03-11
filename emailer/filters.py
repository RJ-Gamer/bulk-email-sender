"""
filterset classes
"""
import django_filters
from django.db.models.functions import TruncDate, TruncMonth, TruncWeek
from django.utils import timezone
from emailer.models import DailyReport


class DailyReportFilter(django_filters.FilterSet):
    """
    filter set for daily reports
    """

    date = django_filters.CharFilter(method="filter_by_date")

    class Meta:
        """
        Meta information
        """

        model = DailyReport
        fields = ["date"]

    def filter_by_date(self, queryset, name, value):
        today = timezone.now().date()
        if value == "daily":
            truncated_date = TruncDate("record_date")
        elif value == "weekly":
            truncated_date = TruncWeek("record_date")
        elif value == "monthly":
            truncated_date = TruncMonth("record_date")
        else:
            return queryset.none()
        queryset = queryset.annotate(truncated_date=truncated_date)
        return queryset.filter(truncated_date=today)
