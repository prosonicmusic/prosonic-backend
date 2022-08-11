# Generated by Django 4.1 on 2022-08-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0014_rename_file_id_product_files"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="daw",
            field=models.CharField(
                blank=True,
                choices=[("cubase", "Cubase"), ("flstudio", "FL Studio")],
                max_length=100,
                null=True,
            ),
        ),
    ]