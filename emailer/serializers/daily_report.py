"""
Serializer for daily reports
"""
from rest_framework import serializers
from emailer.models import DailyReport


class DailyReportSerializer(serializers.ModelSerializer):
    """
    serializer for daily reports
    """

    class Meta:
        """Meta information for daily reports"""

        model = DailyReport
        fields = "__all__"
