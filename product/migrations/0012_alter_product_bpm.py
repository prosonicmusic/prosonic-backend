# Generated by Django 4.1 on 2022-08-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0011_remove_product_overall_price_alter_product_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="bpm",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]