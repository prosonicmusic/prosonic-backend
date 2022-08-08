from dataclasses import Field
from django.contrib import admin
from .models import *


@admin.register(File)
class CustomFile(admin.ModelAdmin):
    list_display = ("file_name", "demo_file")


@admin.register(Product)
class CustomProduct(admin.ModelAdmin):
    list_display = ("file_id", "title", "product_type")
