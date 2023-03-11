"""
Email Validator View
"""
from rest_framework import status, viewsets
from rest_framework.response import Response
from common import constants, functions
from emailer.serializers import EmailValidatorSerializer


class EmailValidatorViewSet(viewsets.ViewSet):
    """
    View Set for validating email addresses from an input file (Excel or CSV).
    """

    serializer_class = EmailValidatorSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        """
        POST method for validating email addresses from an input file.

        Args:
        - request: HttpRequest object containing the input data and metadata
            - input_file(str): The input file path
            - file_type(str): The file type

        Returns:
        - Response object containing a message and data (valid and invalid email addresses)

        Raises:
        - ValidationError: if input data fails to validate against serializer
        """

        # Validate input data against serializer
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract validated data from serializer
        input_file = serializer.validated_data.get("input_file")
        file_type = serializer.validated_data.get("file_type")

        # Get valid and invalid email addresses from input file based on file type
        if file_type in constants.EXCEL_TYPES:
            (
                valid_emails,
                invalid_emails,
            ) = functions.get_valid_and_invalid_emails_from_excel(input_file)
        if file_type in constants.CSV_TYPES:
            valid_emails, invalid_emails = functions.get_valid_invalid_emails_from_csv(
                input_file
            )

        # Return response with message and data (valid and invalid email addresses)
        return Response(
            {
                "message": constants.MSG_SUCCESS,
                "data": {
                    "valid_emails": valid_emails,
                    "invalid_emails": invalid_emails,
                },
            },
            status=status.HTTP_200_OK,
        )
