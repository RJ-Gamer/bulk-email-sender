"""
choice fields
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class FileTypeChoice(models.TextChoices):
    """
    Choice field to choose file type
    """

    XLSX = ".xlsx", _(".xlsx")
    XLS = ".xls", _(".xls")
    CSV = ".csv", _(".csv")
