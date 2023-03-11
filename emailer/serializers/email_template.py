"""
Email Template serializer
"""

from rest_framework import serializers
from emailer.models import EmailTemplate


class EmailTemplateSerializer(serializers.ModelSerializer):
    """
    Email Template serializer
    """

    class Meta:
        """
        Meta information
        """

        model = EmailTemplate
        fields = "__all__"
