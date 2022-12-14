# Generated by Django 4.1 on 2022-08-25 14:12

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
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
                    "demo_file",
                    models.FileField(max_length=254, upload_to="uploads/files/demo"),
                ),
                (
                    "file",
                    models.FileField(max_length=254, upload_to="uploads/files/main"),
                ),
                (
                    "stem",
                    models.FileField(
                        blank=True,
                        max_length=254,
                        null=True,
                        upload_to="uploads/files/stem",
                    ),
                ),
                (
                    "cover",
                    models.FileField(
                        blank=True,
                        max_length=254,
                        null=True,
                        upload_to="uploads/files/cover",
                    ),
                ),
                ("file_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "daw",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Package", "Package"),
                            ("Cubase", "Cubase"),
                            ("FLStudio", "FLStudio"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("length", models.CharField(blank=True, max_length=100, null=True)),
                ("genre", models.CharField(blank=True, max_length=100, null=True)),
                ("bpm", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "project_description",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                (
                    "file_description",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                (
                    "project_image",
                    models.ImageField(
                        blank=True,
                        max_length=254,
                        null=True,
                        upload_to="uploads/images/products",
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        max_length=254,
                        null=True,
                        upload_to="uploads/images/products",
                    ),
                ),
                ("tag", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "product_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Track", "Track"),
                            ("Service", "Service"),
                            ("Package", "Package"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "package_type",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "sample_type",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "product_price",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=10, null=True
                    ),
                ),
                (
                    "stem_price",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=10, null=True
                    ),
                ),
                (
                    "cover_price",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=10, null=True
                    ),
                ),
                ("sold", models.BooleanField(default=False)),
                (
                    "files",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.file",
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]
