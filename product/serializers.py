from itertools import product
from rest_framework import serializers

from prosonic_backend_core.validators import validate_decimals
from .models import File, Product
from prosonic_backend_core import settings


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "demo_file"]


class ProductSerializer(serializers.ModelSerializer):
    files = FileSerializer()
    product_price = serializers.IntegerField()
    stem_price = serializers.IntegerField()
    cover_price = serializers.IntegerField()

    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
