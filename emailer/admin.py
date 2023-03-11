from django.contrib import admin

# Register your models here.
from .models import EmailTemplate, BulkEmailer, DailyReport


admin.site.register(EmailTemplate)
admin.site.register(BulkEmailer)
admin.site.register(DailyReport)
