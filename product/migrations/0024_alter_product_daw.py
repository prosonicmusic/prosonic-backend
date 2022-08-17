# Generated by Django 4.1 on 2022-08-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0023_alter_product_daw_alter_product_product_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="daw",
            field=models.CharField(
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
    ]