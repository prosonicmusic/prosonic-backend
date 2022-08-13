# Generated by Django 4.1 on 2022-08-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0015_alter_product_daw"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="daw",
            field=models.CharField(
                blank=True,
                choices=[("Cubase", "Cubase"), ("FL Studio", "FL Studio")],
                max_length=100,
                null=True,
            ),
        ),
    ]
