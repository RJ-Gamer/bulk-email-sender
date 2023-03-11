"""
bulk mailer view set
"""

from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from common.functions import (
    get_valid_invalid_emails_from_excel,
    get_valid_invalid_emails_from_csv,
)
from common import constants, email_thread, functions
from emailer.models import BulkEmailer
from emailer.serializers import BulkEmailerSerializer


class BulkEmailerViewSet(viewsets.ModelViewSet):
    """
    Bulk Emailer view set
    """

    serializer_class = BulkEmailerSerializer
    queryset = BulkEmailer.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Post method
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_file = serializer.validated_data.get("input_file")
        template = serializer.validated_data.get("template")
        file_type = serializer.validated_data.get("file_type")
        if file_type in constants.EXCEL_FILE_TYPES:
            valid_emails, invalid_emails = get_valid_invalid_emails_from_excel(
                input_file
            )
        if file_type in constants.CSV_FILE_TYPES:
            valid_emails, invalid_emails = get_valid_invalid_emails_from_csv(input_file)
        email_sender = email_thread.EmailThread(
            subject=template.subject,
            body=template.body,
        )
        success_count, failed_count = email_sender.send_emails(
            receiver_list=valid_emails
        )
        daily_record = functions.get_daily_report_object()
        daily_record.total_count += len(valid_emails)
        daily_record.success_count += success_count
        daily_record.failed_count += failed_count
        daily_record.total_requests += 1
        daily_record.save_success_rate
        email_template = serializer.save(
            valid_emails=len(valid_emails),
            invalid_emails=len(invalid_emails),
            mails_sent=success_count,
            mails_failed=failed_count,
        )
        daily_record.save()
        return Response(
            {"message": constants.MSG_SUCCESS.format(""), "data": serializer.data},
            status=status.HTTP_200_OK,
        )
