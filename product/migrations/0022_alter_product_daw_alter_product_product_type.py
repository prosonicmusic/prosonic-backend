# Generated by Django 4.1 on 2022-08-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0021_alter_product_product_type_alter_product_stem_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="daw",
            field=models.CharField(
                blank=True,
                choices=[("Cubase", "Cubase"), ("FL Studio", "FLStudio")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("track", "Track"),
                    ("service", "Service"),
                    ("package", "Package"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]