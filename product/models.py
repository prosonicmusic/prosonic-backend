from asyncore import file_dispatcher
from operator import mod
from django.db import models

# Create your models here.


class File(models.Model):
    demo_file = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.file_name


class Product(models.Model):
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    daw = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    bpm = models.CharField(max_length=100)
    project_description = models.CharField(max_length=100)
    project_image = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100, blank=True)
    package_type = models.CharField(max_length=100, blank=True)
    sample_type = models.CharField(max_length=100, blank=True)
    product_price = models.CharField(max_length=100, blank=True)
    stem_price = models.CharField(max_length=100, blank=True)
    cover_price = models.CharField(max_length=100, blank=True)
    overall_price = models.CharField(max_length=100, blank=True)
    sold = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
