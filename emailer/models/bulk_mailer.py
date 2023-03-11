"""
Bulk emailer model
"""
from random import choices
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from .email_template import EmailTemplate
from common.choices import FileTypeChoice


class BulkEmailer(models.Model):
    """
    Bulk emailer model
    """

    input_file = models.FileField(
        _("File"),
        help_text=_("please upload excel or csv file"),
        validators=[FileExtensionValidator(allowed_extensions=["csv", "xls", "xlsx"])],
        upload_to="emailed_files",
    )
    file_type = models.CharField(
        _("File Type"), max_length=10, choices=FileTypeChoice.choices
    )
    template = models.ForeignKey(
        EmailTemplate, related_name="bulk_mailers", on_delete=models.CASCADE
    )
    valid_emails = models.IntegerField(
        _("Valid Emails"), default=0, help_text="Number of valid emails from the file"
    )
    invalid_emails = models.IntegerField(
        _("Invalid Emails"),
        default=0,
        help_text="Number of invalid emails from the file",
    )
    mails_sent = models.IntegerField(
        _("Mails Sent"),
        default=0,
        help_text="Number of successful emails sent from the valid emails",
    )
    mails_failed = models.IntegerField(
        _("Mails Failed"),
        default=0,
        help_text="Number of failed emails sent from the valid emails",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.input_file.name}"
