# Generated by Django 4.1.7 on 2023-03-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmailTemplate",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "subject",
                    models.CharField(
                        db_index=True,
                        max_length=255,
                        unique=True,
                        verbose_name="Subject",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "body_type",
                    models.CharField(
                        choices=[("Plain Text", "Plain Text"), ("html", "HTML")],
                        max_length=25,
                        verbose_name="Body type",
                    ),
                ),
                ("body", models.TextField(verbose_name="Body")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
            ],
        ),
    ]
