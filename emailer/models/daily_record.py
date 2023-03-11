"""
Record daily count of emails sent and failed
"""
from email.policy import default
from turtle import update
from django.db import models
from django.utils.translation import gettext_lazy as _


class DailyReport(models.Model):
    """
    Record daily count of emails sent and failed
    """

    record_date = models.DateField(_("record_date"), null=True, blank=True)
    total_count = models.IntegerField(
        _("total count"), default=0, help_text="Total count of emails sent"
    )
    success_count = models.IntegerField(
        _("success count"), default=0, help_text="Total count of successful emails sent"
    )
    failed_count = models.IntegerField(
        _("failed count"), default=0, help_text="Total count of failed emails"
    )
    success_rate = models.FloatField(
        _("success rate"), default=0.0, help_text="Success rate of emails sent"
    )
    total_requests = models.IntegerField(
        _("Total Requests"), default=0, help_text="Total number of valid emails"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.record_date} | {self.success_rate}"

    @property
    def save_success_rate(self):
        self.success_rate = (self.success_count / self.total_count) * 100
        self.save()
