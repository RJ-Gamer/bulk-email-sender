"""
Email Validator Serializer
"""
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from common import constants
from common.choices import FileTypeChoice


class EmailValidatorSerializer(serializers.Serializer):
    """
    Email Validator serializer
    """

    input_file = serializers.FileField()
    file_type = serializers.ChoiceField(choices=FileTypeChoice.choices)

    def validate_input_file(self, value):
        """
        Validate the input file attribute.
        """
        if value:
            if (
                value.name.endswith(".csv")
                or value.name.endswith(".xlsx")
                or value.name.endswith(".xls")
            ):
                return value
            raise serializers.ValidationError(_(constants.ERR_INVALID_FILE_TYPE))
        raise serializers.ValidationError(
            _(constants.ERR_NO_INPUT.format(constants.INPUT_FILE))
        )
