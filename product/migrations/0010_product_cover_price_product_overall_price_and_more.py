# Generated by Django 4.1 on 2022-08-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0009_remove_product_cover_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="cover_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="overall_price",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="product_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="stem_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
