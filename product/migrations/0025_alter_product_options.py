# Generated by Django 4.1 on 2022-08-18 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0024_alter_product_daw"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["-id"]},
        ),
    ]