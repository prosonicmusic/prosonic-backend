from nis import cat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import traceback
from rest_framework import status, generics
from product.models import Product
from product.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class ProductPageSizePagination(PageNumberPagination):
    page_size = 20


class ProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tag", "daw", "product_type", "product_price"]
    pagination_class = ProductPageSizePagination
    # permission_classes = [IsAuthenticated]
