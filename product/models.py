from asyncore import file_dispatcher
from operator import mod
from typing_extensions import Self
from django.db import models

# Create your models here.


class File(models.Model):
    demo_file = models.FileField(upload_to=f"uploads/files/demo", max_length=254)
    file = models.FileField(upload_to=f"uploads/files/main", max_length=254)
    file_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.file_name


DAW_CHOICES = (
    ("Cubase", "Cubase"),
    ("FL Studio", "FL Studio"),
)


class Product(models.Model):
    files = models.ForeignKey(File, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    daw = models.CharField(max_length=100, choices=DAW_CHOICES, blank=True, null=True)
    length = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    bpm = models.CharField(max_length=100, blank=True, null=True)
    project_description = models.CharField(max_length=100)
    project_image = models.ImageField(
        upload_to=f"uploads/images/products", max_length=254, blank=True, null=True
    )
    thumbnail = models.ImageField(
        upload_to=f"uploads/images/products", max_length=254, blank=True, null=True
    )
    tag = models.CharField(max_length=100, blank=True, null=True)
    product_type = models.CharField(max_length=100, blank=True, null=True)
    package_type = models.CharField(max_length=100, blank=True, null=True)
    sample_type = models.CharField(max_length=100, blank=True, null=True)
    product_price = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    stem_price = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    cover_price = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    sold = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
