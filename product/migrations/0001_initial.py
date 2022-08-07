# Generated by Django 4.1 on 2022-08-07 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("author", models.CharField(max_length=100)),
                ("daw", models.CharField(max_length=100)),
                ("length", models.CharField(max_length=100)),
                ("genre", models.CharField(max_length=100)),
                ("bpm", models.CharField(max_length=100)),
                ("project_description", models.CharField(max_length=100)),
                ("project_image", models.CharField(max_length=100)),
                ("thumbnail", models.CharField(max_length=100)),
                ("tag", models.CharField(max_length=100)),
                ("product_type", models.CharField(max_length=100)),
                ("package_type", models.CharField(max_length=100)),
                ("sample_type", models.CharField(max_length=100)),
                ("product_price", models.CharField(max_length=100)),
                ("stem_price", models.CharField(max_length=100)),
                ("cover_price", models.CharField(max_length=100)),
                ("overall_price", models.CharField(max_length=100)),
                ("sold", models.CharField(max_length=100)),
            ],
        ),
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
                ("demo_file", models.CharField(max_length=100)),
                ("file", models.CharField(max_length=100)),
                ("file_name", models.CharField(max_length=100)),
                (
                    "product_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]