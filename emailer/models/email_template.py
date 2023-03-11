"""
Email template model
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class EmailTemplate(models.Model):
    """
    Email Template Model
    """

    name = models.CharField(_("Name"), max_length=255)
    subject = models.CharField(_("Subject"), max_length=255, unique=True, db_index=True)
    slug = models.SlugField(
        _("Slug"), max_length=255, unique=True, null=True, blank=True
    )
    body_type = models.CharField(
        _("Body type"),
        max_length=25,
        choices=(("Plain Text", "Plain Text"), ("html", "HTML")),
    )
    body = models.TextField(_("Body"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}: {self.subject}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
