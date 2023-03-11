"""
bulk mailer serializer
"""

from rest_framework import serializers
from emailer.models import BulkEmailer, EmailTemplate


class BulkEmailerSerializer(serializers.ModelSerializer):
    """
    Model Serializer for bulk emailer
    """

    template = serializers.PrimaryKeyRelatedField(queryset=EmailTemplate.objects.all())

    class Meta:
        """
        meta information
        """

        model = BulkEmailer
        fields = "__all__"
    