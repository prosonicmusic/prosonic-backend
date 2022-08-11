from itertools import product
from rest_framework import serializers
from .models import *
from prosonic_backend_core import settings


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
