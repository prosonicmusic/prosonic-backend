# Generated by Django 4.1 on 2022-08-11 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0013_alter_product_project_image_alter_product_thumbnail"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="file_id",
            new_name="files",
        ),
    ]
