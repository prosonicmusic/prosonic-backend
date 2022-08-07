from asyncore import file_dispatcher
from operator import mod
from django.db import models

# Create your models here.
class Product(models.Model):
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
    product_type = models.CharField(max_length=100)
    package_type = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    stem_price = models.CharField(max_length=100)
    cover_price = models.CharField(max_length=100)
    overall_price = models.CharField(max_length=100)
    sold = models.BooleanField(default=False)


class File(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    demo_file = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
