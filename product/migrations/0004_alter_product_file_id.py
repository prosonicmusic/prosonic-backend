# Generated by Django 4.1 on 2022-08-08 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_remove_file_product_id_product_file_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="file_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="product.file"
            ),
        ),
    ]