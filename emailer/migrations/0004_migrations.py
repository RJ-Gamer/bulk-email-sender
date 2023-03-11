# Generated by Django 4.1.7 on 2023-03-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emailer", "0003_migrations"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "record_date",
                    models.DateField(blank=True, null=True, verbose_name="record_date"),
                ),
                (
                    "total_count",
                    models.IntegerField(
                        default=0,
                        help_text="Total count of emails sent",
                        verbose_name="total_count",
                    ),
                ),
                (
                    "success_count",
                    models.IntegerField(
                        default=0,
                        help_text="Total count of successful emails sent",
                        verbose_name="success_count",
                    ),
                ),
                (
                    "failed_count",
                    models.IntegerField(
                        default=0,
                        help_text="Total count of failed emails",
                        verbose_name="failed_count",
                    ),
                ),
                (
                    "success_rate",
                    models.FloatField(
                        default=0.0,
                        help_text="Success rate of emails sent",
                        verbose_name="success_rate",
                    ),
                ),
                (
                    "total_emails",
                    models.IntegerField(
                        default=0,
                        help_text="Total number of valid emails",
                        verbose_name="total_emails",
                    ),
                ),
            ],
        ),
    ]