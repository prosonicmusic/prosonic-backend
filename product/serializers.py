from itertools import product
from rest_framework import serializers
from .models import File, Product
from prosonic_backend_core import settings


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "demo_file"]


class ProductSerializer(serializers.ModelSerializer):
    files = FileSerializer()

    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
