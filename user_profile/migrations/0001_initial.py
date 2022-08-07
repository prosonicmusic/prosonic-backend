# Generated by Django 4.1 on 2022-08-07 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("avatar", models.URLField(max_length=300)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("provice", models.CharField(blank=True, max_length=100, null=True)),
                ("verified", models.CharField(blank=True, max_length=100, null=True)),
                ("otp", models.IntegerField(blank=True, null=True)),
                ("otp_expire_time", models.DateTimeField(blank=True, null=True)),
                (
                    "user_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]